from bit import Key



my_key = Key()


print(my_key.version)

# private_key
print(my_key.to_wif())

# public_key
print(my_key.address)