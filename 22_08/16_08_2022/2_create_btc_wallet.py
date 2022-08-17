from bit import PrivateKeyTestnet

my_key = PrivateKeyTestnet()

print(my_key.version)

print(my_key.to_wif())

print(my_key.address)