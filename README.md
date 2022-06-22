# solana.py Test Code

## 22.06.16 목
    - keypair 조회
    - lamports -> SOL 단위로 convert
    - spl-token Transfer 시도
    - All That Node free blockchain API 사용 테스트
        - api call 은 늘어나는데, sol transfer가 안됨. 잔액조회 등 가능했음
        - response : "Node is Unhealthy"

## 22.06.17 금
    - 최근에 devnet에서 민트한 토큰 1000개 token address 정보 조회
    - solana bootcamp - Day 1 영상 참조 python code 예제 따라해보면서 필요한 정보 추출
        - 토큰 정보 (json)
        - 데이터에 접근 -> 토큰정보(json)['result']['value']['data'][0]
        - 추출한 데이터 b64decode
        - Mint Authority 주소 값 추출 -> 처음 발행했던 주소 일치 확인
        - token 발행량 확인 -> lamports 단위에서 sol단위로 변환
        - token decimal 확인

## 22.06.20 월
    - 1_user_token_getBalance
        - 현재 테스트 토큰을 보유하고 있는 account를 조회하여 토큰 보유량 확인 -> uiValue 값 접근 가능해서 변환해줄 필요 없음. 
    - 2_user_token_transfer
        - 6월17일에 작성한 spl-token transfer 함수로 만들어서 서버에서 ajax test 완료 후 정상작동
    - 3_token_amount
        - 유저가 UI에서 입력할 해당 토큰의 출금수량은 int값이어서 lamports 단위로 변환해야하는데, 관련된 코드
    - 4_get_min_balance_rent_for_exempt_for_account
        - 새로운 어카운트를 생성해주고, 이 어카운트에 rent비용을 계산한 SOL 을 전송해줘야한다.
        - create_account 에 관련된 코드
        - 이제 initialize 만 해서 토큰과 연결해주고 owner 를 토큰을 전송해줄 지갑의 주소로 소유권을 변경해주면 토큰전송을 python 코드로 완성시킬 수 있을 것 같다.
        - 4번을 통해 생성된 transaction
            - https://solscan.io/tx/3ekssQADM9mTNKbLgzg3ukkYzmb1fBYEHLy2JLuxRimNqApTTNyxzX9cAda28JSeoLsM2Gv2ttX5Zvwbj5tf14Qf?cluster=devnet
        - initialize 까지 끝나면 내가 원하는 transaction
            - https://solscan.io/tx/2MYaMvhKzH16gPQUF1WqiZy5K1qRzBDKsrfUGUBRwHixAwWMSuu2EyzV9Q7kr6FaPuc7bsraLRJ8gGjzSJtxaPyC?cluster=devnet

## 22.06.21 화
- create_associate_token_account 생성 성공
    - 어제 성공한 create_account 는 mint address가 연결 되어있지 않고, owner도 이전되지 않은 account여서 테스트토큰을 주고 받을 수 있는 유효한 주소가 아니었다.
    - 오늘 solana.labs에 있는 python코드를 확인. 하지만 async/await 방식으로 비동기적으로 작성되어 있어서 실행방법 및 문법 이해에 어려움이 생겼다.
    - 함수 안에서는 4개의 인자를 받을 수 있는 것으로 파악. 예를 들어 mint:PublicKey, 에서 PublicKey는 변수를 의미하는 것이 아니라 받을 인자의 type을 의미하는 것으로 이해.
    - pycharm 디버깅 모드로 넣어줄 인자별 type 맞는 지 체크 후 앞에서 발견한 async/await 함수를 일반 client 방식으로 변경-> python 파일 실행 시키고 mint address, owner 변경 된 token account 생성 확인
    - solscan tx조회, wallet_address 검색하여 token account owner 변경되어서 해당 지갑주소에 연동 된 것 확인
- reference 
    - https://github.com/solana-labs/solana-program-library/blob/master/stake-pool/py/spl_token/actions.py
    - https://github.com/michaelhly/solana-py/blob/2c45353cb510bfeb7259fa19dacbaefe6b9ae3d1/src/spl/token/client.py#L173
    - https://docs.rs/spl-associated-token-account/latest/spl_associated_token_account/fn.create_associated_token_account.html
    - https://devpouch.tistory.com/189
    - https://spl.solana.com/associated-token-account
    - https://stackoverflow.com/questions/71325517/solana-spl-token-transfer-with-python
    - https://michaelhly.github.io/solana-py/spl/token/client/#spl.token.client.Token.create_associated_token_account
- create_associate_token_account 생성 성공 후 발생한 트랜잭션
    - https://solscan.io/tx/x3a6sPpU22PDWNU16Lgm16ywSM1s364WbzhGukNTEcTgBpSxPXHTwLvTN7V81LCER2rhyuvenLqRB2nUAm4AZSB?cluster=devnet

## 22.06.22 수
- 22.06.21 화 에서 성공한 create_associate_token_account 부분에서 associate_token_account 값 추출해내는 과정을 통해서 값을 얻어내어 DB에 저장을 하고 해당 유저별 tokenAcc에 접근하여 토큰 전송을 할 때 fromAddr(=source) 에 사용위함
- associate_token_account 값을 추출해는 방법 2가지 
    - 1. 서버에서 create_associate_token_account 에 대한 트랜잭션이 완료된 후 생성된 txHash값을 이어서 get_transaction 안에 넣어주고 return되는 json 값 안에서  create_associate_token_account 주소를 찾아내는 방법
        - time.sleep(100)을 줘도 fail이 떠서 의아했다. 왜냐하면 pending이 오래 걸리지 않기 때문이었다.
        - 퇴근 후 집에서 원인 찾음 : 원인은 solana.py 버전의 문제. 저번에 solana.py의 최신버전 0.24.0 버전은 Account()로 새로운 account를 생성불가 됐던 것이 기억이나서 데스크탑에 설치된 solana.py 버전 체크
            - (1) 로컬, 서버 solana version 체크
                - 로컬: 0.23.3
                - 서버: 0.17.0
                - 0.17.0 버전은 Account() 는 됐지만, get_transaction 제공이 안되는 것 확인. 그래서 time.sleep을 많이 부여해줘도 제공자체가 안됐기 때문에 fail이 났던 것 
            - (2) 로컬에서 테스트 후 서버에서 리테스트
                - 로컬 pip uninstall solana →  pip install solana~=0.17.0 → 새로운 지갑 생성 (ts-code) → get_transaction, get_token_accounts_by_owner 테스트
                - 결과 : 0.17.0 버전에서도 get_token_accounts_by_owner 는 작동한다.
                - 추가 테스트 로컬 0.17.0 버전에서 get_transaction 되는지 
                - 결과: get_transaction 이 안된다.
                - 나중에 txList 뽑아내려면 get_transaction 을 해야하는데, 0.17.0 버전이면 안되니까 0.23.0 버전으로 재설치 진행
    - 2. 서버에서 get_token_accounts_by_owner를 사용하는 방법 -> 처음에는 사용 방법을 몰랐다.
        - 집에서 quicknode 사이트에서 reference 찾음
        - https://www.quicknode.com/docs/solana/getTokenAccountsByOwner
        - `from solana.rpc.types import TokenAccountOpts` 를 추가로 import 해줘야한다.
        - 그래서 owner에 대한 publickey를 넣어줘도 opts가 없다고 에러가 발생했었던 것.