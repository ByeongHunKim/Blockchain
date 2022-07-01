from bitcoinlib.wallets import wallet_create_or_open

w = wallet_create_or_open('wallet1', network='bitcoin', witness_type='segwit')
n_utxos = w.utxos_update()
if n_utxos:
    print("Found new unspent outputs (UTXO's), we are ready to create a transaction")
print(w.info())