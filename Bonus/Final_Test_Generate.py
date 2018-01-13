import math
import random, string
import warnings
import sys, os
import pyprimes
import hashlib
import DSA, TxBlockGen, PoW

TxBlocksGenOn = 1    # set to 1 if you want to generate a block of bitcoin transaction
PoWGenOn = 1         # set to 1 if you want to provide PoW for given transaction blocks

blockCount = int(sys.argv[2]) # number of link in the block chain (you can change)
TxCount = 8    # number of transactions in a block (you can change, but set it to a power of two)
PoWLen = 6     # the number of 0s in PoW (you can change)
TxLen = 10     # no of lines in a transaction (do not change)
LinkLen = 4    # no of lines in a link of the chain (do not change)

# Generate a random transaction along with its signature
if TxBlocksGenOn:
    if os.path.exists('DSA_params.txt') == True:
        inf = open('DSA_params.txt', 'r')
        q = int(inf.readline())
        p = int(inf.readline())
        g = int(inf.readline())
        inf.close()
        print "DSA parameters are read from file DSA_params.txt"
    else:
        print 'DSA_params.txt does not exist'
        sys.exit()

    FileName = "TransactionBlock"
    for i in range(int(sys.argv[1]),int(sys.argv[1])+blockCount):
        transaction=TxBlockGen.GenTxBlock(p, q, g, TxCount)
        TxBlockFileName = FileName+str(i)+".txt"
        TxBlockFile = open(TxBlockFileName, "w")
        TxBlockFile.write(transaction)
        TxBlockFile.close()
        print "Transaction block %d is written into TransactionBlock%d.txt" %(i,i)

# Proof of work generation for given transcation blocks
if PoWGenOn:
    FileName = "TransactionBlock"
    ChainFileName = "LongestChain.txt"
    for i in range(int(sys.argv[1]),int(sys.argv[1])+blockCount):
        TxBlockFileName = FileName+str(i)+".txt"
        if os.path.exists(TxBlockFileName) == True:
            PoW.PoW(TxBlockFileName, ChainFileName, PoWLen, TxLen)
            print "Proof of work is written/appended to "+ ChainFileName
        else:
            print "Error: ", TxBlockFileName, "does not exist"
            sys.exit()
