import random
from utils import generate_rand_permutation


def algoritmo_construtivo_aleatorizado(m, conjuntos):

    re = generate_rand_permutation(m)

    # Inicializa variáveis
    c = 0  # Variável de controle de elementos cobertos
    solucao = []  # Lista para armazenar a solução

    # Enquanto c for diferente do total de m elementos
    while c < m:
        # Pega o próximo elemento não coberto de re
        itera = iter(solucao)
        prox = next(itera)
        elemento = next((x for x in re if x not in solucao), None)

        if elemento is not None:
            # Gera permutação p com os subconjuntos que cobrem o elemento
            conjuntos_cobrem_elemento = [s for s in conjuntos if elemento in s]
            random.shuffle(conjuntos_cobrem_elemento)

            # Seleciona o primeiro subconjunto s que cobre o elemento
            s = conjuntos_cobrem_elemento[0]

            # Coloca subconjunto s na solução e atualiza solução
            solucao.append(s)

            # Verifica se s cobre outros elementos não cobertos e atualiza c
            for e in s:
                if e not in solucao:
                    c += 1
        else:
            break  # Todos os elementos foram cobertos

    return solucao


# Exemplo de uso
m = 10  # Número total de elementos
conjuntos = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}]
re = generate_rand_permutation(m)
print("Elementos")
print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("permutação aleatória")
print(re)
print("Conjuntos")
print(conjuntos)

solucao = algoritmo_construtivo_aleatorizado(m, conjuntos)
print("Solução")
print(solucao)


#solucao = algoritmo_construtivo_aleatorizado(m, conjuntos)
#print("Solução:", solucao)
