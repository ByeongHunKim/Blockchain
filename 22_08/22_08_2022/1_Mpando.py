import environ
from web3 import Web3, HTTPProvider
import pickle

env = environ.Env()
environ.Env.read_env()

MPANDO_URL = env('MPANDO_URL')
# print(MPANDO_URL)

web3 = Web3(HTTPProvider(MPANDO_URL))


print("web3 - Connection : ", web3.isConnected())







