from bitcoinlib.wallets import wallet_create_or_open

w = wallet_create_or_open('bitcoinlib-testnet1', network='testnet', witness_type='segwit')

# wk = w.new_key()
# print("Deposit to address %s to get started" % wk.address)

# t = w.send_to('tb1qvpth63fd3u26m4mnhlgdn5wj0r2pdxczl55km0', 5000, fee=2000)
# sendBtc = t.info()
# print(sendBtc)

# n_utxos = w.utxos_update()
# if n_utxos:
#     print("Found new unspent outputs (UTXO's), we are ready to create a transaction")


# w.utxos_update()
# t = w.sweep('tb1qvpth63fd3u26m4mnhlgdn5wj0r2pdxczl55km0', min_confirms=0)
# print(t.info())

print(w.info())
result = w.get_key()
print(result.address)

