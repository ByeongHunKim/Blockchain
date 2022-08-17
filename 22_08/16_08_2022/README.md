- HOW TO START
  - pip install bit
  - pip install django-environ~=0.9.0

```
import environ

env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('FROMUSER_PRIVKEY')
```
