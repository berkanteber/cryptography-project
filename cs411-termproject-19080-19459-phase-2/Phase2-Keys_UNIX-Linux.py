############################################################################################################
# Project Group:                                                                                          ##
# 19080 - Berkan Teber                                                                                    ##
# 19459 - Arda Olmezsoy                                                                                   ##
############################################################################################################
# Important Note:                                                                                         ##
# This program has been written and executed in UNIX.                                                     ##
############################################################################################################
# Program prints out the execution time, which is approximately 30 seconds, as standard output.           ##
# Program also generates 2 files:                                                                         ##
#                           1- DSA_skey.txt, which contains q, p, g and alpha                             ##
#                           2- DSA_pkey.txt, which contains q, p, g and beta                              ##                     ##
############################################################################################################

import time
from random import seed, randint

def main():
    seed("19080-19459") # to obtain the same results

    params = open("DSA_params.txt")

    # get previously computed parameters
    qpg = []
    for line in params:
        qpg.append(int(line))
    q, p, g = qpg

    params.close()

    # compute alpha and beta
    alpha = randint(1, q - 1)
    beta = pow(g, alpha, p)

    # write to files

    skey = open("DSA_skey.txt", "w")
    skey.write(str(q) + "\n")
    skey.write(str(p) + "\n")
    skey.write(str(g) + "\n")
    skey.write(str(alpha) + "\n")
    skey.close()

    pkey = open("DSA_pkey.txt", "w")
    pkey.write(str(q) + "\n")
    pkey.write(str(p) + "\n")
    pkey.write(str(g) + "\n")
    pkey.write(str(beta) + "\n")
    pkey.close()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print "Execution Time: %s seconds" % (end_time - start_time)
