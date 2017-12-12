############################################################################################################
# Project Group:                                                                                          ##
# 19080 - Berkan Teber                                                                                    ##
# 19459 - Arda Olmezsoy                                                                                   ##
############################################################################################################
# Important Note:                                                                                         ##
# This program has been written and executed in UNIX.                                                     ##
############################################################################################################

import sys
import random
import hashlib

if sys.version_info < (3, 6):
    import sha3

# obtained from the resources
def BasicTest(n, q, k):
    a = random.randint(2, n-1)
    x = pow(a, q, n)
    if x == 1 or x == n-1:
            return 1
    for i in range(1, k):
        x = pow(x,2,n)
        if x == 1:
            return -1
        if x == n-1:
            return 1
    return -1

# obtained from the resources
def MRTest(n, t):
    k = 0
    q = n-1
    while (q%2==0):
        q = q/2
        k+=1
    while (t>0):
        t = t-1
        if BasicTest(n, q, k)==1:
            continue
        else:
            return -1
    return 1

# obtained from the resources
def PrimalityTest(n,t):
    small_primes = [2, 3, 5, 7, 11, 13]

    for i in small_primes:
        if n%i==0:
            return -1
    return MRTest(n, t)

# generates q, p and alpha as defined in the lecture slides
def DL_Param_Generator(small_bound, large_bound):
    while True:
        q = random.randint(0, small_bound - 1)
        if PrimalityTest(q, 10) == 1:
            break

    while True:
        p = q * random.randint(0, int(large_bound / small_bound)) + 1
        if PrimalityTest(p, 10) == 1:
            break

    while True:
        alpha = random.randint(0, p - 1)
        g = pow(alpha, (p-1) / q, p)
        if g != 1:
            break

    return q, p, g

# generates alpha and beta as defined in the homework document
def KeyGen(p, q, g):
    alpha = random.randint(1, q - 1)
    beta = pow(g, alpha, p)

    return (alpha, beta)

# generates signatures r and s as defined in the homework document
def SignGen(m, p, q, g, alpha, beta):
    h = int(hashlib.sha3_256(m).hexdigest(), 16)
    h = h % q

    k = random.randint(1, q - 1)
    r = pow(g, k, p)

    s = (alpha * r + k * h) % q

    return (r, s)

# taken from the homework 4 document
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# taken from the homework 4 document
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# verifies the signature as defined in the homework document
def SignVer(m, r, s, p, q, g, beta):
    h = int(hashlib.sha3_256(m).hexdigest(), 16)
    h = h % q

    v = modinv(h, q)

    z1 = (s * v) % q
    z2 = ((q - r) * v) % q

    u = (pow(g, z1, p) * pow(beta, z2, p)) % p

    if (r % q) == (u % q):
        return 1
    return -1
