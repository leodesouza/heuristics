def create_greedy_constructive(subconjuntos):
    elementos_cobertos = set()
    elementos_restantes = set()
    for subconjunto in subconjuntos:
        elementos_restantes.update(subconjunto)

    num_elementos_cobertos = 0
    solucao = []

    subconjuntos_ordenados = sorted(subconjuntos, key=lambda x: sum(x))

    while elementos_restantes:
        menor_subconjunto = None
        menor_custo = float('inf')
        for subconjunto in subconjuntos_ordenados:
            custo_subconjunto = sum(subconjunto)
            if custo_subconjunto < menor_custo and any(elem not in elementos_cobertos for elem in subconjunto):
                menor_custo = custo_subconjunto
                menor_subconjunto = subconjunto

        elementos_cobertos.update(menor_subconjunto)
        for elem in menor_subconjunto:
            elementos_restantes.discard(elem)
        num_elementos_cobertos += len(menor_subconjunto)
        solucao.append(menor_subconjunto)

    return solucao, num_elementos_cobertos

# Exemplo de uso
# subconjuntos = [
#     [1, 2, 3],  # Custo: 6
#     [2, 4],  # Custo: 6
#     [1, 3, 5],  # Custo: 9
#     [4, 5]  # Custo: 9
# ]
#
# solucao, num_elementos_cobertos = construtivo_guloso(subconjuntos)
#
# print("Solução encontrada:")
# for subconjunto in solucao:
#     print(subconjunto)
#
# print("\nNúmero de elementos cobertos:", num_elementos_cobertos)
