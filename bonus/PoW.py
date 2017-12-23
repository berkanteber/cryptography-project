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

# appends pow and other related data to the chain for a given transaction
def PoW(TxBlockFileName, ChainFileName, PoWLen, TxLen):
    chain = open(ChainFileName, "a+")
    chainstring = ""

    # find and append the previous hash value

    chain.seek(0)
    lasthash = "Day Zero Link in the Chain"
    for line in chain:
        lasthash = line[:-1]
    chainstring += lasthash + "\n"

    block = open(TxBlockFileName, "r")

    # compute and append the root hash value of the merkle tree

    lines = []
    for line in block:
        lines.append(line)

    TxCount = len(lines) / TxLen

    hashes = []
    for i in range(TxCount):
        transaction = "".join(lines[i * TxLen : (i+1) * TxLen])
        hashed = hashlib.sha3_256(transaction).hexdigest()
        hashes.append(hashed)

    while len(hashes) > 1:
        newhashes = []
        for i in range(len(hashes) / 2):
            tobehashed = hashes[2 * i] + hashes[2 * i + 1]
            hashed = hashlib.sha3_256(tobehashed).hexdigest()
            newhashes.append(hashed)
        hashes = newhashes

    roothash = hashes[0]
    chainstring += roothash + "\n"

    # compute and append nonce and pow

    while True:
        nonce = str(random.randint(0, 2**128 - 1)) + "\n"
        possible = chainstring + nonce
        hashed = hashlib.sha3_256(possible).hexdigest()

        check = True
        for i in range(PoWLen):
            if hashed[i] != "0":
                check = False

        if check == True:
            chainstring = possible + hashed + "\n"
            chain.write(chainstring)
            break

    block.close()
    chain.close()
