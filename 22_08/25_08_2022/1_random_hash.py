import secrets

random_hash = secrets.token_hex(nbytes=32)
random_txHash = "pando0x" + random_hash
print(random_txHash)