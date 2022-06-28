import asyncio
from solana.rpc.async_api import AsyncClient
 
ENDPOINT = "https://api.devnet.solana.com"
PUBKEY = ""
 
 
async def main():
    async with AsyncClient(ENDPOINT) as client:
        res = await client.is_connected()
        if res:
            balance = await client.get_balance(PUBKEY)
 
    print(balance)
 
 
asyncio.run(main())