import random

# 일반, 레어, 전설 등급
samples = ["ipfs://awdawdawd/0.json","ipfs://awdawdawd/2.json", "ipfs://awdawdawd/3.json"]

# 일반: 70% 레어25%, 전설5%
random_nft = random.choices(samples, weights=(70, 25, 5))[0]

print("random_nft", random_nft)