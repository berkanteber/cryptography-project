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

import sys
import time
from random import seed, randint

import MillerRabinTestByErkaySavas

def main():
    seed("19080-19459")

    smallbit = 256
    largebit = 2048

    params = open("DSA_params.txt", "w")

    ctrq = 1
    while True:
        q = randint(2**(smallbit-1), 2**smallbit - 1)

        if MillerRabinTestByErkaySavas.PrimalityTest(q, 10) == 1:
            params.write(str(q) + "\n")
            print "q has been found in " + str(ctrq) + " steps."
            break

        ctrq += 1

    ctrp = 1
    while True:
        p = q * randint(2**(largebit-smallbit-1), 2**(largebit-smallbit)) + 1

        if MillerRabinTestByErkaySavas.PrimalityTest(p, 10) == 1:
            params.write(str(p) + "\n")
            print "p has been found in " + str(ctrp) + " steps."
            break

        ctrp += 1

    ctrg = 1
    while True:
        alpha = randint(0, p - 1)

        g = pow(alpha, (p-1) / q, p)
        if g != 1:
            params.write(str(g) + "\n")
            print "g has been found in " + str(ctrg) + " steps."
            break

        ctrg += 1

    params.close()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print "Execution Time: %s seconds" % (end_time - start_time)
