# sudo apt-get install libgmp-dev
# pip3 install fastecdsa
# pip install bitcoinlib

from bitcoinlib.wallets import Wallet

w = Wallet.create('Wallet1')
key1 = w.get_key()
print(key1.address)