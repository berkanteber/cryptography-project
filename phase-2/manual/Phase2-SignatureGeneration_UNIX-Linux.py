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

import sys
import time
import hashlib
from random import seed, randint

if sys.version_info < (3, 6):
    import sha3

def main():
    seed("19080-19459") # to obtain the same results

    # get previously computed parameters
    params = open("DSA_params.txt")
    qpg = []
    for line in params:
        qpg.append(int(line))
    q, p, g = qpg
    params.close()

    # get alpha
    skey = open("DSA_skey.txt")
    for line in skey:
        alpha = int(line)
    skey.close()

    # get beta
    pkey = open("DSA_pkey.txt")
    for line in pkey:
        beta = int(line)
    pkey.close()

    transaction = open("SingleTransaction.txt", "w")

    # write the title, the serial number, the payer, the payee and the amount

    string = "*** Bitcoin transaction ***\n"

    # serial is a random 128-bit integer
    serial = randint(0, 2**128 - 1)
    string += "Serial number: " + str(serial) + "\n"

    payer = hex(randint(0, 2**40 - 1))[2:].upper()
    string += "Payer: " + payer + "\n"

    payee = hex(randint(0, 2**40 - 1))[2:].upper()
    string += "Payee: " + payee + "\n"

    amount = randint(1, 1000)
    string += "Amount: " + str(amount) + " Satoshi" + "\n"

    # write the parameters

    string += "p: " + str(p) + "\n"
    string += "q: " + str(q) + "\n"
    string += "g: " + str(g) + "\n"

    # write the public key

    string += "Public Key (beta): " + str(beta) + "\n"

    # compute signature

    h = int(hashlib.sha3_256(string).hexdigest(), 16)
    h = h % q

    k = randint(1, q - 1)
    r = pow(g, k, p)

    s = (alpha * r + k * h) % q

    # write signature

    string += "Signature (r): " + str(r) + "\n"
    string += "Signature (s): " + str(s) + "\n"

    # write to the file
    transaction.write(string)

    transaction.close()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print "Execution Time: %s seconds" % (end_time - start_time)
