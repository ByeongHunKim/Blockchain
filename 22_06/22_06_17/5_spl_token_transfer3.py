from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction

import os
from dotenv import load_dotenv

class TransferService:
    def __init__(self, client: Client, service: SolanaService, token) -> None:
        self.client = client
        self.service = service
        self.keypair = self.service.get_keypair(token)

    def make_transaction(self, source, mint, dest, owner, amount=1, decimals=0) -> Transaction:
        transaction = Transaction()
        transaction.add(transfer_checked(
            TransferCheckedParams(
                program_id=TOKEN_PROGRAM_ID,
                mint=PublicKey(mint),
                source=PublicKey(source),
                dest=PublicKey(dest),
                owner=owner,
                amount=amount,
                decimals=decimals,
                signers=[]
        )))
        return transaction

    def send_transaction(self, transaction) -> None:
        self.client.send_transaction(
            transaction,
            self.keypair,
            opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed)
        )

load_dotenv()

if __name__ == "__main__":
    token = os.getenv('TOKEN')
    client = Client('https://api.devnet.solana.com')
    service = SolanaService(client)
    token = os.getenv('KEYPAIR')
    transfer = TransferService(client, service, token)
    a = client.get_account_info(transfer.keypair.public_key)
    transaction = transfer.make_transaction(
        source='',
        mint='',
        dest='',
        owner=transfer.keypair.public_key,
        amount=1,
        decimals=9

    )
    transfer.send_transaction(transaction)


# reference 

# https://stackoverflow.com/questions/71325517/solana-spl-token-transfer-with-python

# pip install python-dotenv