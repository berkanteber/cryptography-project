Project Group:

19080 - Berkan Teber
19459 - Arda Olmezsoy

--------------------------------

Important Note:

The program included in this homework is written and executed in UNIX.

--------------------------------

Files and Explanations:

  Phase1_UNIX.py:

  This is the main program for Phase 1, written and executed in UNIX.
  To run, execute the following command on the terminal: python2 Phase1_UNIX.py

  In this program, 5 initial accounts has been generated.
  Then, 10 transactions have been performed between a random payer-payee pair, with a random amount.

  Program prints out the execution time, which is approximately 25 minutes, as standard output.

  Program also generates 2 files:

    1- LongestChain.txt:

        This file is the requested output file in the homework document.
        It contains the bitcoin transactions with the following:
            - Serial Number
            - Payer
            - Payee
            - Amount
            - Previous Hash
            - Nonce
            - Proof of Work

    2- AccountBalances.txt:

        This file includes the initial and final balances of the accounts as well as the balances after each transaction.

  ValidateChain.py:

  This is the provided program to check the correctness of the results.
  To run, execute the following command on the terminal: python2 ValidateChain.py > IsChainValidated.txt

  With this command, IsChainValidated.txt is generated.
  You can check this file and see that the produced output generates a valid chain.
