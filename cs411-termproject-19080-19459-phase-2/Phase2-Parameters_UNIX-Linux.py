############################################################################################################
# Project Group:                                                                                          ##
# 19080 - Berkan Teber                                                                                    ##
# 19459 - Arda Olmezsoy                                                                                   ##
############################################################################################################
# Important Note:                                                                                         ##
# This program has been written and executed in UNIX.                                                     ##
############################################################################################################
# Program prints out the execution time, which is approximately 25 minutes, as standard output.           ##
# Program also generates the file DSA_params.txt, which is the requested file.                            ##
############################################################################################################

import sys
import time
from random import seed, randint

import MillerRabinTest-ProvidedInResources

if sys.version_info < (3, 6):
    import sha3

def main():
    seed("19080-19459")





if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print "Execution Time: %s seconds" % (end_time - start_time)
