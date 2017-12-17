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

def GenTxBlock(p, q, g, TxCount):
    bigstring = ""

    for i in range(TxCount):
        string = "*** Bitcoin transaction ***\n"

        serial = random.randint(0, 2**128 - 1)
        string += "Serial number: " + str(serial) + "\n"

        string += "p: " + str(p) + "\n"
        string += "q: " + str(q) + "\n"
        string += "g: " + str(g) + "\n"

        payer_alpha = random.randint(1, q - 1)
        payer_beta = pow(g, payer_alpha, p)

        string += "Payer Public Key (beta): " + str(payer_beta) + "\n"

        payee_alpha = random.randint(1, q - 1)
        payee_beta = pow(g, payee_alpha, p)

        string += "Payee Public Key (beta): " + str(payee_beta) + "\n"

        amount = random.randint(1, 1000)
        string += "Amount: " + str(amount) + " Satoshi" + "\n"

        # compute signature

        h = int(hashlib.sha3_256(string).hexdigest(), 16)
        h = h % q

        k = random.randint(1, q - 1)
        r = pow(g, k, p)

        s = (payer_alpha * r + k * h) % q

        string += "Signature (r): " + str(r) + "\n"
        string += "Signature (s): " + str(s) + "\n"

        bigstring += string

    return bigstring
