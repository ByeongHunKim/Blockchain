- HOW TO START
  - pip install bit
  - pip install django-environ~=0.9.0

```
import environ

env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('FROMUSER_PRIVKEY')
```

- reference
	- https://nownodes.io/blog/how-to-make-a-bitcoin-transaction-with-python/
	- https://ofek.dev/bit/
	- https://github.com/ofek/bit/blob/master/bit/format.py
	- https://bitcoinfaucet.uo1.net/send.php
