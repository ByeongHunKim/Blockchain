# testnet 
from bit import PrivateKeyTestnet

# using env file 
import environ
env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('FROMUSER_PRIVKEY')
my_key = PrivateKeyTestnet(fromUserPriv)

my_key_tx_history = my_key.get_transactions()

print(my_key_tx_history)

#output
#['9035cca9076eaef9b2ddb3d89605afde9cc81961f0b0e06b637bf4492307c84c', 
#'26a89e4f8b5db622cd4445a70c08911fd788376f78785689efaa38bf76d8bb5c', '81c98dcb075366fc1c7db6185b7f3c39f5ff96f7e5611bbfe8c9ffe4e922092c', 
#'b6542980414f0ecbdb2742e69a16dd4ce94720034a303747c00599b5d675a806', '730c62edabfd1922f097df51b3147457729f05a8a5d0ceae0e0847bd0bfa93b6']