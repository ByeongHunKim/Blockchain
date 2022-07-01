from bitcoinlib.wallets import wallet_create_or_open

w = wallet_create_or_open('bitcoinlib-testnet1', network='testnet', witness_type='segwit')
t = w.send_to('tb1qprqnf4dqwuphxs9xqpzkjdgled6eeptn389nec', 4000, fee=1000)
print(t.info())