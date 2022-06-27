from solana.rpc.api import Client
from solana.publickey import PublicKey


client = Client("https://snowy-still-flower.solana-mainnet.quiknode.pro/")

# client = Client("https://dark-black-frog.solana-devnet.quiknode.pro/")

print(client.get_account_info(PublicKey('')))

