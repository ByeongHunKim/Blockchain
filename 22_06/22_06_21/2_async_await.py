# None 타입으로 리턴한다고 주석달고 1 리턴
def test(x:int)->None:
    print("test")
    return 1
    
# int형을 매개변수로 준다하면서 문자열 전달
print(test("str"))


async def create_associated_token_account(
    client: AsyncClient,
    payer: Keypair,
    owner: PublicKey,
    mint: PublicKey
) -> PublicKey:
    txn = Transaction()
    create_txn = spl_token.create_associated_token_account(
        payer=payer.public_key, owner=owner, mint=mint
    )
    txn.add(create_txn)
    await client.send_transaction(txn, payer, opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))
    return create_txn.keys[1].pubkey

    print(create_associated_token_account())