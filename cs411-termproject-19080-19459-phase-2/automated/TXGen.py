############################################################################################################
# Project Group:                                                                                          ##
# 19080 - Berkan Teber                                                                                    ##
# 19459 - Arda Olmezsoy                                                                                   ##
############################################################################################################
# Important Note:                                                                                         ##
# This program has been written and executed in UNIX.                                                     ##
############################################################################################################
# Program prints out the execution time, which is approximately 25 minutes, as standard output.           ##
# Program also generates the file SignatureTransaction.txt, which is the requested file.                  ##
############################################################################################################

import random
import hashlib

def GenSingleTx(p, q, g, alpha, beta):
    string = "*** Bitcoin transaction ***\n"

    serial = random.randint(0, 2**128 - 1)
    string += "Serial number: " + str(serial) + "\n"

    payer = hex(random.randint(0, 2**40 - 1))[2:].upper()
    string += "Payer: " + payer + "\n"

    payee = hex(random.randint(0, 2**40 - 1))[2:].upper()
    string += "Payee: " + payee + "\n"

    amount = random.randint(1, 1000)
    string += "Amount: " + str(amount) + " Satoshi" + "\n"

    string += "p: " + str(p) + "\n"
    string += "q: " + str(q) + "\n"
    string += "g: " + str(g) + "\n"

    string += "Public Key (beta): " + str(beta) + "\n"

    # compute signature

    h = int(hashlib.sha3_256(string).hexdigest(), 16)
    h = h % q

    k = random.randint(1, q - 1)
    r = pow(g, k, p)

    s = (alpha * r + k * h) % q

    string += "Signature (r): " + str(r) + "\n"
    string += "Signature (s): " + str(s) + "\n"

    return string
