# Guarda as informações de um voo
class DadosVoo:

    def __init__(
        self,
        preco,
        aeroporto_origem,
        aeroporto_destino,
        data_ida,
        data_volta
    ):
        self.preco = preco
        self.aeroporto_origem = aeroporto_origem
        self.aeroporto_destino = aeroporto_destino
        self.data_ida = data_ida
        self.data_volta = data_volta


# Procura o voo mais barato
def encontrar_voo_mais_barato(
    dados,
    data_volta
):
    # Verifica se a API retornou algum voo
    if (
        dados is None
        or (
            not dados.get("best_flights")
            and not dados.get("other_flights")
        )
    ):
        print("Nenhum voo encontrado.")

        return DadosVoo(
            "N/A",
            "N/A",
            "N/A",
            "N/A",
            "N/A"
        )

    # Junta todos os voos encontrados
    todos_voos = (
        dados.get("best_flights", [])
        + dados.get("other_flights", [])
    )

    primeiro_voo = todos_voos[0]

    menor_preco = primeiro_voo["price"]

    aeroporto_origem = (
        primeiro_voo["flights"][0]
        ["departure_airport"]["id"]
    )

    aeroporto_destino = (
        primeiro_voo["flights"][-1]
        ["arrival_airport"]["id"]
    )

    data_ida = (
        primeiro_voo["flights"][0]
        ["departure_airport"]["time"]
        .split(" ")[0]
    )

    voo_mais_barato = DadosVoo(
        menor_preco,
        aeroporto_origem,
        aeroporto_destino,
        data_ida,
        data_volta
    )

    # Compara todos os preços
    for voo in todos_voos:

        try:
            preco = voo["price"]

        except KeyError:
            print(
                "Esse voo não possui preço disponível."
            )
            continue

        if preco < menor_preco:
            menor_preco = preco

            aeroporto_origem = (
                voo["flights"][0]
                ["departure_airport"]["id"]
            )

            aeroporto_destino = (
                voo["flights"][-1]
                ["arrival_airport"]["id"]
            )

            data_ida = (
                voo["flights"][0]
                ["departure_airport"]["time"]
                .split(" ")[0]
            )

            voo_mais_barato = DadosVoo(
                menor_preco,
                aeroporto_origem,
                aeroporto_destino,
                data_ida,
                data_volta
            )

    return voo_mais_barato