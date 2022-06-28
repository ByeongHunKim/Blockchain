@csrf_exempt
def createAssociateTokenAcc(request):
    try:
        import spl.token.instructions as spl_token
        from solana.rpc.types import TokenAccountOpts
        test = client.is_connected()
        print("1. 솔라나 연결여부:" ,test)
        userID = request.POST.get('userID')
        print("2. 현재 유저의 id: ",userID)
        userinfo = SignUp.objects.get(id = userID)
        print("3. 현재 유저의 정보 :",userinfo)
        userTokenAcc = userinfo.solTokenAcc
        feePayerWalletAddr = "" # feePayer : mint address의 주인 
        feePayerPriv = "" # feePayer : mint address 주인의 privkey
        feePayerKeypair = b58decode(feePayerPriv)
        feePayer = Keypair.from_secret_key(feePayerKeypair)
        owner1 = userinfo.userPubKey
        ownerPub = PublicKey(owner1)
        mint1 = '' # 고정값
        mintPub = PublicKey(mint1)
        # transaction 시작
        if userTokenAcc == "0" :
            transaction = Transaction()
            create_txn = spl_token.create_associated_token_account(
                payer=feePayerWalletAddr, owner=ownerPub, mint=mintPub
            )
            transaction.add(create_txn)
            print("4. transaction 값 : ", transaction)
            result = client.send_transaction(transaction, feePayer)
            resultOfTxn = result['result']
            print(f"5.txHash = https://solscan.io/tx/{resultOfTxn}?cluster=devnet")
            time.sleep(20)
            queryTokenAcc = client.get_token_accounts_by_owner(ownerPub,TokenAccountOpts(mint=mint1))
            getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
            print(f"6.새로 생성된 account 주소 = {getTokenAcc}")
            userinfo.userPubKey = getTokenAcc
            userinfo.save()
        else : 
            print("이미 계좌가 존재합니다 == ",userTokenAcc)
        context = {'value' : '1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('실패')
        context = {'valule':'-99'}
        return HttpResponse(json.dumps(context))

@csrf_exempt
def getBalanceToken(request):
    try:
        test = client.is_connected()
        print("1. 솔라나 연결여부:" ,test)
        userID = request.POST.get('userID')
        print("2. 현재 유저의 id: ",userID)
        userinfo = SignUp.objects.get(id = userID)
        print("3. 현재 유저의 정보 :",userinfo)
        # 유저의토큰어카운트 = userinfo.유저의 토큰어카운트주소
        userTokenAcc = userinfo.solTokenAcc
        if userTokenAcc !== "0" :
            print("--------------------토큰어카운트 보유-------------------------")
            print("4. 현재 유저의 토큰어카운트 :",userTokenAcc)
            result = client.get_token_account_balance(userTokenAcc) 
            ui_tokenVal = result['result']['value']['uiAmount']
            print("5. 현재 유저의 토큰 잔액은? : ", ui_tokenVal)
            userinfo.solTokenVal = ui_tokenVal
            userinfo.save()
        else : 
            print("실패 ------------ 토큰어카운트를 보유하고 있지 않습니다.----------")
        context = {'value' : '1','ui_tokenVal' : 'ui_tokenVal'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('실패')
        context = {'valule':'-99'}
        return HttpResponse(json.dumps(context))

@csrf_exempt
def tokenTransfer(request):
    try:
        from spl.token.constants import TOKEN_PROGRAM_ID
        from spl.token.instructions import transfer_checked, TransferCheckedParams
        test = client.is_connected()
        print("1. 솔라나 연결여부:" ,test)
        userID = request.POST.get('userID')
        print("2. 현재 유저의 id: ",userID)
        userinfo = SignUp.objects.get(id = userID)
        print("3. 현재 유저의 정보 :",userinfo)
        mintPubkey = "" # mint address (고정값)
        userTokenAcc = userinfo.solTokenAcc
        tokenAccOwner = userinfo.userPubKey
        fromAddr = userinfo.solTokenAcc
        fromAddrPriv = userinfo.userPrivKey
        fromAddrKeypair = b58decode(fromAddrPriv)
        print("2. b58decode privkey: ", fromAddrKeypair)
        signer = Keypair.from_secret_key(fromAddrKeypair) # 서명자 
        print("3. signkey: ", signer)
        toAddr = "" # 3. toAddr = 유저가 token 출금페이지에서 입력한 주소 -> dest 값
        amount = float(50) # 유저가 token 출금페이지에서 입력한 금액 -> dest 값
        print("4. amount: ", amount)
        transfer_amount = int(amount*(10**9)) # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
        print("5. transfer_amount: ", transfer_amount)
        # transaction 시작
        if userTokenAcc !== "0" :
            print("전송시작")
            transaction = Transaction()
            transaction.add(transfer_checked(
                TransferCheckedParams(
                    amount=transfer_amount,
                    decimals=9,
                    dest=PublicKey(toAddr),
                    mint=PublicKey(mintPubkey),
                    owner=PublicKey(tokenAccOwner),
                    program_id=TOKEN_PROGRAM_ID,
                    source=PublicKey(fromAddr),
                    )))
            print("6. transaction: ", transaction)
            transaction_result = client.send_transaction(transaction, signer)
            print("7. transaction_result: ", transaction_result)
            resultOfTxHash = transaction_result['result']
            print("8. resultOfTxHash: ", resultOfTxHash)
            print(f"9. 성공한 txHash = https://solscan.io/tx/{resultOfTxHash}?cluster=devnet")
        else if : 
            print("토큰어카운트를 보유하고 있지 않은 유저입니다.")
        context = {'value' : '1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('실패')
        context = {'valule':'-99'}
        return HttpResponse(json.dumps(context))