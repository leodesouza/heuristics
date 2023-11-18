import random

def mymalloc(size):
    s = malloc(size)
    if s is None:
        print("\nERRO memoria")
        print("malloc : Not enough memory.")
        exit(EXIT_FAILURE)
    return s

def error_reading_file(text):
    print(text)
    exit(EXIT_FAILURE)

# L'Ecuyer random number generator
def rando():
    global x10, x11, x12, x20, x21, x22
    x10, x11, x12, x20, x21, x22 = 12345, 67890, 13579, 24680, 98765, 43210

    m = 2147483647
    m2 = 2145483479
    a12, q12, r12 = 63308, 33921, 12979
    a13, q13, r13 = -183326, 11714, 2883
    a21, q21, r21 = 86098, 24919, 7417
    a23, q23, r23 = -539608, 3976, 2071
    invm = 4.656612873077393e-10

    h = x10 // q13
    p13 = -a13 * (x10 - h * q13) - h * r13
    h = x11 // q12
    p12 = a12 * (x11 - h * q12) - h * r12

    if p13 < 0:
        p13 += m
    if p12 < 0:
        p12 += m

    x10, x11, x12 = x11, x12, (p12 - p13) % m
    if x12 < 0:
        x12 += m

    h = x20 // q23
    p23 = -a23 * (x20 - h * q23) - h * r23
    h = x22 // q21
    p21 = a21 * (x22 - h * q21) - h * r21

    if p23 < 0:
        p23 += m2
    if p21 < 0:
        p21 += m2

    x20, x21, x22 = x21, x22, (p21 - p23) % m2
    if x22 < 0:
        x22 += m2

    if x12 < x22:
        h = x12 - x22 + m
    else:
        h = x12 - x22

    if h == 0:
        return 1.0
    else:
        return h * invm

# Return an integer between low and high
def unif(low, high):
    return low + int((high - low + 1) * rando())

# Test the random number generator
for _ in range(10):
    print(rando())
