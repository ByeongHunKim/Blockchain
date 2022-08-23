- `$ pip install pickle-mixin`
- `$ mkdir eth-transactions-web3py && cd eth-transactions-web3py && echo > transaction_finder.py`

- import pickle
- from web3 import Web3, HTTPProvider

- poa chain 에러발생 시

```
from web3.middleware import geth_poa_middleware
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
```

### resference site

- https://www.quicknode.com/guides/web3-sdks/how-to-fetch-transaction-history-on-ethereum-using-web3-py
- https://ethereum.stackexchange.com/questions/88274/how-to-get-list-of-transactions-history-about-specific-contract-address-using-we
- https://web3py.readthedocs.io/en/stable/web3.eth.html#web3.eth.Eth.getBlock
- https://ethereum.stackexchange.com/questions/88274/how-to-get-list-of-transactions-history-about-specific-contract-address-using-we
- https://stackoverflow.com/questions/48477949/not-able-to-pip-install-pickle-in-python-3-6
