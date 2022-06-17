from base58 import b58encode, b58decode
from solana.keypair import Keypair

# 4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3 's privkey
feePayer = ""
keypair = b58decode(feePayer)

keypair.public_key

private_key = keypair[:32]
public_key = keypair[32:]

# wallet_address = b58encode(public_key) -> b'4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3'

wallet_address = b58encode(public_key).decode()
# 4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3

print("1.keypair : ", keypair.public_key)
print("2.public_key : ", public_key)
print("3.private_key : ", private_key)
print("4.wallet_address : ", wallet_address)


