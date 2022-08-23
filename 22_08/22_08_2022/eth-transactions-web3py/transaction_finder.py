
#import dependencies
import pickle
from web3 import Web3, HTTPProvider
import environ

env = environ.Env()
environ.Env.read_env()
MPANDO_URL = env('MPANDO_URL')
MY_ADDR= env('MY_ADDR')


#instantiate a web3 remote provider
web3 = Web3(HTTPProvider(MPANDO_URL))


from web3.middleware import geth_poa_middleware
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

print("web3 - Connection : ", web3.isConnected())

#request the latest block number
ending_blocknumber = web3.eth.blockNumber

#latest block number minus 100 blocks
starting_blocknumber = ending_blocknumber - 4000

#filter through blocks and look for transactions involving this address
blockchain_address = MY_ADDR

#create an empty dictionary we will add transaction data to
tx_dictionary = {}

def getTransactions(start, end, address):
    '''This function takes three inputs, a starting block number, ending block number
    and an Ethereum address. The function loops over the transactions in each block and
    checks if the address in the to field matches the one we set in the blockchain_address.
    Additionally, it will write the found transactions to a pickle file for quickly serializing and de-serializing
    a Python object.'''
    print(f"Started filtering through block number {start} to {end} for transactions involving the address - {address}...")
    for x in range(start, end):
        block = web3.eth.getBlock(x, True)
        for transaction in block.transactions:
            if transaction['to'] == address or transaction['from'] == address:
                # with open("transactions.pkl", "wb") as f:
                print("-"*100)
                hashStr = transaction['hash'].hex()
                print("hashStr", hashStr)
                print("-"*100)
                tx_dictionary[hashStr] = transaction
                print("tx_dictionary", tx_dictionary)
                # print(tx_dictionary['from'])
                print("transaction---------------------------->", transaction)
                print(transaction['from'])
                print("-"*100)
                # pickle.dump(tx_dictionary, f)
                # f.close()
    print(f"Finished searching blocks {start} through {end} and found {len(tx_dictionary)} transactions")
    

getTransactions(starting_blocknumber, ending_blocknumber, blockchain_address)