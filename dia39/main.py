from datetime import datetime, timedelta
import requests_cache

from gerenciador_dados import GerenciadorDados
from pesquisa_voos import PesquisaVoos
from dados_voo import encontrar_voo_mais_barato
from gerenciador_notificacoes import GerenciadorNotificacoes


# Cria um cache para evitar muitas chamadas às APIs
requests_cache.install_cache(
    "cache_voos",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600
    }
)


# Aeroporto de origem
CODIGO_AEROPORTO_ORIGEM = "LHR"

# Datas da pesquisa
amanha = datetime.now() + timedelta(
    days=1
)

seis_meses = datetime.now() + timedelta(
    days=6 * 30
)


# Cria os objetos do programa
gerenciador_dados = GerenciadorDados()

pesquisa_voos = PesquisaVoos()

notificacoes = GerenciadorNotificacoes()


# Busca os destinos da planilha
destinos = gerenciador_dados.buscar_destinos()


# Pesquisa cada destino
for destino in destinos:

    print()
    print(
        f"Pesquisando voos para "
        f"{destino['city']}..."
    )

    dados_voos = pesquisa_voos.verificar_voos(
        codigo_origem=CODIGO_AEROPORTO_ORIGEM,
        codigo_destino=destino["iataCode"],
        data_ida=amanha,
        data_volta=seis_meses
    )

    voo_mais_barato = encontrar_voo_mais_barato(
        dados_voos,
        data_volta=seis_meses.strftime(
            "%Y-%m-%d"
        )
    )

    print(
        f"{destino['city']}: "
        f"GBP {voo_mais_barato.preco}"
    )

    # Verifica se encontrou um preço válido
    if voo_mais_barato.preco == "N/A":
        continue

    # Verifica se o preço encontrado é menor
    # que o valor salvo na planilha
    if (
        voo_mais_barato.preco
        < destino["lowestPrice"]
    ):
        print(
            f"Voo mais barato encontrado para "
            f"{destino['city']}."
        )

        # Atualiza o preço na planilha
        gerenciador_dados.atualizar_menor_preco(
            destino["id"],
            voo_mais_barato.preco
        )

        mensagem = (
            f"Alerta de preço baixo!\n\n"
            f"Somente GBP {voo_mais_barato.preco} "
            f"para voar de "
            f"{voo_mais_barato.aeroporto_origem} "
            f"para "
            f"{voo_mais_barato.aeroporto_destino}.\n\n"
            f"Ida: {voo_mais_barato.data_ida}\n"
            f"Volta: {voo_mais_barato.data_volta}"
        )

        # Envia pelo WhatsApp
        notificacoes.enviar_whatsapp(
            mensagem
        )