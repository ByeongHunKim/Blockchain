from bitcoinlib.services.bitcoind import BitcoindClient

bdc = BitcoindClient.from_config('/home/bstudent/testCode/22_06/22_06_29/bitcoin.conf')
txid = 'e0cee8955f516d5ed333d081a4e2f55b999debfff91a49e8123d20f7ed647ac5'
rt = bdc.getrawtransaction(txid)
print("Raw: %s" % rt)