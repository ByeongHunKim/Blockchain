# solana.py Test Code

- 22.06.16 Thu
    - keypair 조회
    - lamports -> SOL 단위로 convert
    - spl-token Transfer 시도
    - All That Node free blockchain API 사용 테스트
        - api call 은 늘어나는데, sol transfer가 안됨. 잔액조회 등 가능했음
        - response : "Node is Unhealthy"

- 22.06.17 Fri
    - 최근에 devnet에서 민트한 토큰 1000개 token address 정보 조회
    - solana bootcamp - Day 1 영상 참조 python code 예제 따라해보면서 필요한 정보 추출
        - 토큰 정보 (json)
        - 데이터에 접근 -> 토큰정보(json)['result']['value']['data'][0]
        - 추출한 데이터 b64decode
        - Mint Authority 주소 값 추출 -> 처음 발행했던 주소 일치 확인
        - token 발행량 확인 -> lamports 단위에서 sol단위로 변환
        - token decimal 확인