# from bitcoin import *


# print(history("1NprfWgJfkANmd1jt88A141PjhiarT8d9U"))

# sudo apt-get install libgmp-dev
# pip3 install fastecdsa
# pip install bitcoinlib

from bitcoinlib.wallets import Wallet

from base58 import b58encode, b58decode as b58d
b58e = lambda x: b58encode(x).decode('ascii')
from base64 import b64decode as b64d
from bitcoinlib.keys import Key


# w = Wallet.create('Wallet12343ddddddddd')
# key1 = w.get_key()
# print(key1.address)
# print(w.info())

# key1Priv = key1.key_private
# print(key1Priv)

# key1Endode = b58e(key1Priv)
# print(key1Endode)


      
wif = '04def044bee863ea08bf29947cb257016ade9180caca281deb1e804abdcc9e53411fd515bca55e57d4a21655fd167d3d875a4a60677b45fcd681dea5e82c86a73f'
k = Key(wif)

result = k.address()

print(k.info())