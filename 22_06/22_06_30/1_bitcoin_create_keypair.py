# pip install bitcoin

# import bitcoin
from bitcoin import *

# Create Private Key -> 0088bd01802f36675d341f7d59419400b408221b763d47acf9d221920f97dd31
private_key = random_key()
print("1. 생성된 private_key : ",private_key)

# Create Public Key -> 04c1739c087971238e461e017b9ee2326daad02699648c9be4bf1d418b93e34787b2153455d8fca36061d5554039be535af8f8025d0672c83e204abe631e177029
public_key = privtopub(private_key)
print("2. 생성된 public_key : ",public_key)

# Create A Bitcoin Address
address = pubtoaddr(public_key)
print("3. 생성된 bitcoin address : ",address)
# 1Bdz58SG4zqmtf6xM4HR8WbKj5tXG9NrxP

# 첫번째로 생성한 address 조회 -> https://blockchair.com/search?q=1PRz1q3npXLTbLCs4gg5YCJZXVMaWX5CjB&submitButton=