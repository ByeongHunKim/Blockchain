# mainnnet
from bit import Key

# using env file 
import environ
env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('MAINNET_PRIVKEY')
my_key = Key(fromUserPriv)

my_key_tx_history = my_key.get_transactions()

print(my_key_tx_history)