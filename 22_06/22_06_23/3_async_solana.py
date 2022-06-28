# from solana.publickey import PublicKey
# from solana.rpc.async_api import AsyncClient
# import asyncio;




# async def main():
#     print('hhi')
#     await foo()

# async def foo():
#     test = client.is_connected()
#     print(test)

# asyncio.run(main())

from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
import asyncio

solana_client = AsyncClient("https://api.devnet.solana.com")
asyncio.run(solana_client.get_account_info("4Nnk4ffKvjqx5kPH4xUofBrCTvgUuoDnAHBC2b12hYdP"))

