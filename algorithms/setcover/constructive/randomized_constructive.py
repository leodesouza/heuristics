import random
from algorithms.utils.pseudo_random_generator import generate_rand_permutation, create_index


def create_randomized_constructive(scp_sets_instance):
    elements = set()
    for subSet in scp_sets_instance:
        elements.update(subSet)

    shuffled_vector = generate_rand_permutation(len(elements))
    c = 0
    # Inicializa variáveis
    c = 0  # Variável de controle de elementos cobertos
    solucao = []  # Lista para armazenar a solução
    rand_permutation = iter(generated_randon_permutation)
    # Enquanto c for diferente do total de m elementos
    while c < m:
        # Pega o próximo elemento não coberto de rand_permutation
        not_covered_element = next((x for x in rand_permutation if x not in solucao), None)

        if not_covered_element is not None:
            # Gera permutação com os subconjuntos que cobrem o elemento
            sets_that_cover_element = [s for s in scp_sets_instance if not_covered_element in s]
            random.shuffle(sets_that_cover_element)

            # Seleciona o primeiro subconjunto que cobre o elemento
            s = sets_that_cover_element[0]
            c += 1

            # Verifica se s cobre outros elementos não cobertos e atualiza c
            for e in s:
                if e != not_covered_element:
                    found = any(e in sublist for sublist in solucao)
                    if not found:
                        c += 1
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
