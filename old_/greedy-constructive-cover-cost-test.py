def construtivo_guloso_custo_cobertura(subconjuntos):
    elementos_cobertos = set()
    elementos_restantes = set()
    for subconjunto in subconjuntos:
        elementos_restantes.update(subconjunto)

    num_elementos_cobertos = 0
    solucao = []
    subconjuntos_ordenados = []

    for subconjunto in subconjuntos:
        custo_cobertura = len(subconjunto) / len(set(subconjunto) - elementos_cobertos)
        subconjuntos_ordenados.append((custo_cobertura, subconjunto))

    subconjuntos_ordenados.sort(key=lambda x: x[0])

    while elementos_restantes:
        menor_subconjunto = None
        menor_custo = float('inf')
        for subconjunto in subconjuntos_ordenados:
            custo_cobertura, conjunto = subconjunto
            if custo_cobertura < menor_custo and any(elem not in elementos_cobertos for elem in conjunto):
                menor_custo = custo_cobertura
                menor_subconjunto = conjunto

        elementos_cobertos.update(menor_subconjunto)
        for elem in menor_subconjunto:
            elementos_restantes.discard(elem)
        num_elementos_cobertos += len(menor_subconjunto)
        solucao.append(menor_subconjunto)

    return solucao, num_elementos_cobertos

# Exemplo de uso
subconjuntos = [
    [1, 2, 3],  # Custo: 6, Número de elementos: 3
    [2, 4],     # Custo: 6, Número de elementos: 2
    [1, 3, 5],  # Custo: 9, Número de elementos: 3
    [4, 5]      # Custo: 9, Número de elementos: 2
]

solucao, num_elementos_cobertos = construtivo_guloso_custo_cobertura(subconjuntos)

print("Solução encontrada:")
for subconjunto in solucao:
    print(subconjunto)

print("\nNúmero de elementos cobertos:", num_elementos_cobertos)
