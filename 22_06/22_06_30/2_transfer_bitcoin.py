from bitcoinlib.wallets import Wallet

# address1 = "1PRz1q3npXLTbLCs4gg5YCJZXVMaWX5CjB"

# print(address1.info())

userNickname = 'name1'

createWallet = Wallet.create(userNickname)

createWallet.info()

print(createWallet.scan())

# userKey = createWallet.get_key()

# print(userKey.address)
# print(userKey.privkey)
