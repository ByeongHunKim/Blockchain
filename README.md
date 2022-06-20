# solana.py Test Code

- 22.06.16 목
    - keypair 조회
    - lamports -> SOL 단위로 convert
    - spl-token Transfer 시도
    - All That Node free blockchain API 사용 테스트
        - api call 은 늘어나는데, sol transfer가 안됨. 잔액조회 등 가능했음
        - response : "Node is Unhealthy"

- 22.06.17 금
    - 최근에 devnet에서 민트한 토큰 1000개 token address 정보 조회
    - solana bootcamp - Day 1 영상 참조 python code 예제 따라해보면서 필요한 정보 추출
        - 토큰 정보 (json)
        - 데이터에 접근 -> 토큰정보(json)['result']['value']['data'][0]
        - 추출한 데이터 b64decode
        - Mint Authority 주소 값 추출 -> 처음 발행했던 주소 일치 확인
        - token 발행량 확인 -> lamports 단위에서 sol단위로 변환
        - token decimal 확인

- 22.06.20 월
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