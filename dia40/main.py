import requests_cache
from datetime import datetime, timedelta

from gerenciador_dados import GerenciadorDados
from pesquisa_voos import PesquisaVoos
from dados_voo import encontrar_voo_mais_barato
from gerenciador_notificacoes import GerenciadorNotificacoes


# Cria cache para diminuir as chamadas das APIs
requests_cache.install_cache(
    "cache_voos",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600
    }
)


# Aeroporto de origem
CODIGO_ORIGEM = "LHR"

# Define o período da pesquisa
amanha = datetime.now() + timedelta(
    days=1
)

seis_meses = datetime.now() + timedelta(
    days=6 * 30
)


# Cria os objetos
gerenciador_dados = GerenciadorDados()

pesquisa_voos = PesquisaVoos()

notificacoes = GerenciadorNotificacoes()


# Busca os destinos
destinos = gerenciador_dados.buscar_destinos()


# Busca os clientes
clientes = gerenciador_dados.buscar_clientes()


# Monta a lista de e-mails
lista_emails = []

for cliente in clientes:
    email = cliente.get(
        "whatIsYourEmail?"
    )

    if email:
        lista_emails.append(
            email
        )


# Pesquisa cada destino
for destino in destinos:

    print()
    print(
        f"Pesquisando voo direto para "
        f"{destino['city']}..."
    )

    dados_voos = pesquisa_voos.verificar_voos(
        codigo_origem=CODIGO_ORIGEM,
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


    # Caso não encontre voo direto,
    # procura voos com escalas
    if voo_mais_barato.preco == "N/A":

        print(
            "Nenhum voo direto encontrado."
        )

        print(
            "Procurando voo com escala..."
        )

        dados_voos = pesquisa_voos.verificar_voos(
            codigo_origem=CODIGO_ORIGEM,
            codigo_destino=destino["iataCode"],
            data_ida=amanha,
            data_volta=seis_meses,
            somente_direto=False
        )

        voo_mais_barato = encontrar_voo_mais_barato(
            dados_voos,
            data_volta=seis_meses.strftime(
                "%Y-%m-%d"
            )
        )

        print(
            f"Menor preço com escala: "
            f"GBP {voo_mais_barato.preco}"
        )


    # Verifica se encontrou um preço menor
    if (
        voo_mais_barato.preco != "N/A"
        and voo_mais_barato.preco
        < destino["lowestPrice"]
    ):

        gerenciador_dados.atualizar_menor_preco(
            destino["id"],
            voo_mais_barato.preco
        )


        # Monta a mensagem
        if voo_mais_barato.paradas == 0:

            mensagem = (
                "Alerta de preço baixo!\n\n"
                f"Somente GBP {voo_mais_barato.preco} "
                f"para voar diretamente de "
                f"{voo_mais_barato.aeroporto_origem} "
                f"para "
                f"{voo_mais_barato.aeroporto_destino}.\n\n"
                f"Ida: {voo_mais_barato.data_ida}\n"
                f"Volta: {voo_mais_barato.data_volta}"
            )

        else:
            mensagem = (
                "Alerta de preço baixo!\n\n"
                f"Somente GBP {voo_mais_barato.preco} "
                f"para voar de "
                f"{voo_mais_barato.aeroporto_origem} "
                f"para "
                f"{voo_mais_barato.aeroporto_destino}.\n\n"
                f"Paradas: {voo_mais_barato.paradas}\n"
                f"Ida: {voo_mais_barato.data_ida}\n"
                f"Volta: {voo_mais_barato.data_volta}"
            )


        print(
            f"Voo barato encontrado para "
            f"{destino['city']}."
        )


        # Envia pelo WhatsApp
        notificacoes.enviar_whatsapp(
            mensagem
        )


        # Envia para todos os clientes
        notificacoes.enviar_emails(
            lista_emails,
            mensagem
        )