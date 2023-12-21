# *************** L'Ecuyer random number generator ***************
# pseudo random number generator

from config import x10, x11, x12, x20, x21, x22


def lecuyer_rando(seed):
    if seed is not None and seed > 0:
        lecuyer_rando.x12 += seed
    m = 2147483647
    m2 = 2145483479
    a12, q12, r12 = 63308, 33921, 12979
    a13, q13, r13 = -183326, 11714, 2883
    a21, q21, r21 = 86098, 24919, 7417
    a23, q23, r23 = -539608, 3976, 2071
    invm = 4.656612873077393e-10

    h = lecuyer_rando.x10 // q13
    p13 = -a13 * (lecuyer_rando.x10 - h * q13) - h * r13
    h = lecuyer_rando.x11 // q12
    p12 = a12 * (lecuyer_rando.x11 - h * q12) - h * r12

    if p13 < 0:
        p13 += m
    if p12 < 0:
        p12 += m

    lecuyer_rando.x10, lecuyer_rando.x11, lecuyer_rando.x12 = lecuyer_rando.x11, lecuyer_rando.x12, p12 - p13
    if lecuyer_rando.x12 < 0:
        lecuyer_rando.x12 += m

    h = lecuyer_rando.x20 // q23
    p23 = -a23 * (lecuyer_rando.x20 - h * q23) - h * r23
    h = lecuyer_rando.x22 // q21
    p21 = a21 * (lecuyer_rando.x22 - h * q21) - h * r21

    if p23 < 0:
        p23 += m2
    if p21 < 0:
        p21 += m2

    x20, x21, x22 = lecuyer_rando.x21, lecuyer_rando.x22, p21 - p23
    if x22 < 0:
        x22 += m2

    if lecuyer_rando.x12 < x22:
        h = lecuyer_rando.x12 - x22 + m
    else:
        h = lecuyer_rando.x12 - x22

    if h == 0:
        return 1.0
    else:
        return h * invm


# ********* Returns a random integer between low and high (included) ***********/
def create_index(low, high, pseudo_random):
    return low + int((high - low + 1) * pseudo_random)


def generate_rand_permutation(n, pseudo_random):
    p = [i for i in range(n)]
    for i in range(n - 1):
        random_index = create_index(i, n - 1, pseudo_random)
        p[i], p[random_index] = p[random_index], p[i]
    return p


lecuyer_rando.x10, lecuyer_rando.x11, lecuyer_rando.x12 = x10, x11, x12
lecuyer_rando.x20, lecuyer_rando.x21, lecuyer_rando.x22 = x20, x21, x22
