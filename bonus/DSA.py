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
