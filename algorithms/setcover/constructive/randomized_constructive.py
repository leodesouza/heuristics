import random
from utils import generate_rand_permutation


def create_randomized_constructive(conjuntos):
    m = len(conjuntos)
    re = generate_rand_permutation(m)

    # Inicializa variáveis
    c = 0  # Variável de controle de elementos cobertos
    solucao = []  # Lista para armazenar a solução
    iter_re = iter(re)
    # Enquanto c for diferente do total de m elementos
    while c < m:
        # Pega o próximo elemento não coberto de re
        elemento = next((x for x in iter_re if x not in solucao), None)

        if elemento is not None:
            # Gera permutação p com os subconjuntos que cobrem o elemento
            conjuntos_cobrem_elemento = [s for s in conjuntos if elemento in s]
            random.shuffle(conjuntos_cobrem_elemento)

            # Seleciona o primeiro subconjunto s que cobre o elemento
            s = conjuntos_cobrem_elemento[0]

            # Verifica se s cobre outros elementos não cobertos e atualiza c
            found = False
            for e in s:
                for item in solucao:
                    if e in item:
                        found = True
                if not found:
                    c += 1
            # Coloca subconjunto s na solução e atualiza solução
            solucao.append(s)

        else:
            break  # Todos os elementos foram cobertos

    return solucao


# Exemplo de uso
# m = 10  # Número total de elementos
# conjuntos = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 0}, {3, 6, 9}]
# re = generate_rand_permutation(m)
# print("Elementos")
# print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print("permutação aleatória")
# print(re)
# print("Conjuntos")
# print(conjuntos)
#
# solucao = algoritmo_construtivo_aleatorizado(m, conjuntos)
# print("Solução")
# print(solucao)


#solucao = algoritmo_construtivo_aleatorizado(m, conjuntos)
#print("Solução:", solucao)
