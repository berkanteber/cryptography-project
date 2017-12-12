############################################################################################################
# Project Group:                                                                                          ##
# 19080 - Berkan Teber                                                                                    ##
# 19459 - Arda Olmezsoy                                                                                   ##
############################################################################################################
# Important Note:                                                                                         ##
# This program has been written and executed in UNIX.                                                     ##
############################################################################################################
# Program prints out the execution time, which is approximately 30 seconds, as standard output.           ##
# Program also generates the file DSA_params.txt which is the requested file                              ##
############################################################################################################

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

def DL_Param_Generator(small_bound, large_bound):
    while True:
        q = randint(2**(smallbit-1), 2**smallbit - 1)
        if MillerRabinTestByErkaySavas.PrimalityTest(q, 10) == 1:
            break

    while True:
        p = q * randint(2**(largebit-smallbit-1), 2**(largebit-smallbit)) + 1
        if MillerRabinTestByErkaySavas.PrimalityTest(p, 10) == 1:
            break

    while True:
        alpha = randint(0, p - 1)
        g = pow(alpha, (p-1) / q, p)
        if g != 1:
            break

    return q, p, g

def KeyGen(p, q, g):
    alpha = randint(1, q - 1)
    beta = pow(g, alpha, p)

    return (alpha, beta)

def SignGen(p, q, g, alpha, beta):
    string = "*** Bitcoin transaction ***\n"

    serial = randint(0, 2**128 - 1)
    string += "Serial number: " + str(serial) + "\n"

    payer = hex(randint(0, 2**40 - 1))[2:].upper()
    string += "Payer: " + payer + "\n"

    payee = hex(randint(0, 2**40 - 1))[2:].upper()
    string += "Payee: " + payee + "\n"

    amount = randint(1, 1000)
    string += "Amount: " + str(amount) + " Satoshi" + "\n"

    string += "p: " + str(p) + "\n"
    string += "q: " + str(q) + "\n"
    string += "g: " + str(g) + "\n"

    string += "Public Key (beta): " + str(beta) + "\n"

    # compute signature

    h = int(hashlib.sha3_256(string).hexdigest(), 16)
    h = h % q

    k = randint(1, q - 1)
    r = pow(g, k, p)

    s = (alpha * r + k * h) % q

    return (r, s)
