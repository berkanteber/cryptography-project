import sys
import time
import hashlib
from random import seed, randint

if sys.version_info < (3, 6):
    import sha3

# initiate the accounts
def initiate():
    accounts = []

    accounts.append({"name" : "Vincent Chase", "balance" : 20000})
    accounts.append({"name" : "Eric Murphy", "balance" : 3500})
    accounts.append({"name" : "Johnny Chase", "balance" : 1500})
    accounts.append({"name" : "Turtle", "balance" : 5000})
    accounts.append({"name" : "Ari Gold", "balance" : 10000})

    return accounts

# list the names and the balances of all the accounts
def listAccounts(state, accounts, out):
    if state == "Before Any Transaction":
        out.write("#################################\n")

    out.write(state)
    out.write("\n----------------------\n")

    total = 0
    for account in accounts:
        total += account["balance"]
        out.write(account["name"].ljust(16) + str(account["balance"]).rjust(8) + " Satoshi\n")
    out.write("---------------------------------\n")
    out.write("Total".ljust(16) + str(total).rjust(8) + " Satoshi\n")
    out.write("#################################\n")

def main():
    seed("entourage")                                   # to obtain the same results

    ab = open("AccountBalances.txt", "w")               # will contain the balances of the all the accounts after every transaction
    lc = open("LongestChain.txt", "w")                  # will contain the bitcoin transactions as stated in the homework document

    accounts = initiate()                               # initiate the accounts
    listAccounts("Before Any Transaction", accounts, ab)  # list accounts before any transaction

    prevHash = "First transaction"

    # 10 transactions in total
    for i in range(10):
        s = "*** Bitcoin transaction ***\n"

        # serial is a random 128-bit number
        serial = randint(0, 2**128 - 1)
        s+= "Serial number: " + str(serial) + "\n"

        # select a payer, payee and an amount, all randomly
        payer_index, payee_index = -1, -1
        while payer_index == payee_index or accounts[payer_index]["balance"] == 0:
            payer_index = randint(0, len(accounts) - 1)
            payee_index = randint(0, len(accounts) - 1)
        payer, payee, amount = accounts[payer_index]["name"], accounts[payee_index]["name"], randint(1, accounts[payer_index]["balance"])

        s+= "Payer: " + str(payer) + "\n"
        s+= "Payee: " + str(payee) + "\n"

        s+= "Amount: " + str(amount) + "\n"

        s += "Previous hash in the chain: " + prevHash + "\n"

        # find a nonce and compute pow
        while True:
            # nonce is obtained with a random 18-bit integer
            nonce = "Nonce: " + str(randint(0, 2**128 - 1)) + "\n"
            possible = s + nonce

            hashed = hashlib.sha3_256(possible).hexdigest()

            # check if it meets the criteria
            if hashed[:6] == "000000":
                break

        s = possible
        s += "Proof of Work: " + hashed + "\n"

        lc.write(s)

        # perform transaction
        accounts[payer_index]["balance"] -= amount
        accounts[payee_index]["balance"] += amount

        # list accounts after each transaction
        listAccounts("After Transaction #" + str(i+1), accounts, ab)

        prevHash = hashed

    # list accounts after all transactions
    listAccounts("After All Transactions", accounts, ab)

    ab.close()
    lc.close()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print "Execution Time: %s seconds" % (end_time - start_time)
