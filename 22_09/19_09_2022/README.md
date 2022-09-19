# 1. INTRODUCTION

- `Django` 프레임워크가 정말 많은 기능을 가지고 있다.
- `Django`는 매우 객체 지향적인 프레임워크이다.
  - 그래서 객체 지향 프로그래밍의 기본이 필요하다. (OOP)
  - python's class Inheritance Method Constructor에 관한 내용

## Django study를 통해 배울 것

1. `rest API` 와 `graphQL API` 두 개 만들기
2. `Django` 에서 테스트 하는 방법
3. 관리자 패널과 사용자 인증
4. `Django` 에 대한 많은 것
5. `Django`를 deploy하고 , REACTJS로 만든 API들을 효율적으로 사용해볼 것

## 왜 사람들이 Django를 좋아하는 가

- `Django`가 멋진 이유 중 하나는 더 생산적인 개발자로 만들어주기 때문
  - 아주 적은 시간과 노력
  - 그리고 적은 코드로 더 많은 것들을 만들 수 있다
- 웹 개발의 많은 번거로움을 줄여줘서 시간 낭비 없이 앱 코드 작성에 집중할 수 있게 해준다.
- `reinvent`
  - 재창조라는 건, 기본적으로 새로운 상품, 새로운 서비스 등 항상 같은 기능을 반복해서 개발하고 구현해야한다는 걸 의미한다.
  - 예를 들어 새로운 상품을 만든다면, 관리자 패널이 필요할 가능성이 높다. 그리고 사용자들이 필요할 것 ( 로그인, 로그아웃 ) 그리고 사용자 이름, 이메일 그리고 비밀번호가 있을 것
  - 그래서 보안, 로그인, 로그아웃 방법들을 구현해야한다. 이 모든 건 많은 대부분의 웹 어플리케이션들이 필요로 하는 요소다.
  - 또 데이터베이스와 소통하는 방법이 필요하고 마이그레이션을 만들어야 한다.
  - `reinvent` 는 이러한 것들을 반복해서 구현해야된다는 것을 의미한다. 커리어를 쌓고 제품을 많이 만들수록 혹은 만약 창업가이고 다른 여러 서비스들을 구현하고 싶다면,
  - 이런 것들을 반복해서 하게 될 것이다.
  - `Django`는 위에서 언급한 것들을 기본적으로 프레임워크에 내포하고 있다.
    - ex) 관리 패널 -> 제공해주기 때문에 공짜로 사용하기만 하면 된다. 그리고 사용자 인증 -> 제공해준다.
    - 이렇게 `Django`는 어플리케이션의 재밌는 부분을 만드는데에만 집중할 수 있게 해준다.
    - 왜냐하면 나머지는 `Django`가 알아서 하기 때문.
    - `Django`는 일반적인 웹 개발 작업 처리 시 사용할 수 있는 수십개의 항목을 포함한다.
    - 그리고 사용자 인증, 컨텐츠 관리, 사이트 맵, RSS피드 등 많은 작업들을 처리한다.
    - 또한 보안도 처리하고 나를 보호해주기도 한다. 그렇기 때문에 아무것도 할 필요가 없다.
      - SQL 삽입, 사이트 간 스크립팅, 요청위조, 클릭 재킹 같은 일반적인 오류에 대해 기본적으로 안전하고, 아무것도 안해도 보안 요소들을 즐길 수 있다.
- 좋은 확장성
  - 지구상에서 가장 트래픽이 높은 사이트 일부는 `Django`를 이용한다.
  - 인스타그램은 `Django`를 써서 수백만 명의 사용자들로 확장되어있고, 이건 믿을 수 없을 정도로 다재다능하다.
  - 왜냐하면 원하는대로 `Django`를 커스터마이징 할 수 있기 때문이다.

## Flask와 Django의 차이 -> 최소화 vs 극대화

- Flask는 미니멀리스트고 사용하기 매우 쉽다.
  - 작은 레고 블록처럼 부품으로 시작되고 아주 가볍다.
- Django는 장난감으로 가득 찬 박스이다.
  - 많은 장난감(기능)들을 가지고 있기 때문에 무겁다.
- 장난감(기능)들을 다 사용하지 않는다면 , 가득 찬 상자를 들고 다닐 필요가 없다는 부분이 Django와 Flask를 이해해야하는 가장 큰 차이점이다.

- Django는 극대화 되어있고 많은 기능을 가지고 있다. 만약 그것들을 사용하고싶다면 이해하고 사용하기 위해 노력해야한다.

  - 우리가 알아야 할 많은 것들을 가지고 있고 그것들은 훌륭하고 아주 유용하다.
  - 하지만 많은걸 배워야하기 때문에 매우 복잡하기도 하다.
  - Django를 외우고 배우는 건 Flask API보다 많은 시간이 소요된다.

- 원하는게 뭔지 정확히 알아야한다.
  - 만약 관리패널과 ORM 사용자 인증이 필요한 Applicaion을 만들고 싶고 rest API, GraphQL API가 필요하다면, Django를 선택하는 편이 좋다
  - 그렇지않고 아주 작은 서비스 application을 구축해야한다면 (관리패널조차 없는 작은 rest API, 큰 SQL 데이터베이스도 필요없고 아주 작은 rest API, 표면적인 일부만 필요한 경우)

# 2. SET UP

## python3

### python3 download

- `python.org/downloads/`
- download -> run terminal -> `$ python`
- console에서 `$ python` 실행 시 버전이 3으로 보이는지 확인 필요

## consist folder

- `$ mkdir airbnb-clone-backend`
- `$ cd airbnb-clone-backend`
- 만약 레포를 구성하고 싶다면 ? `$ git init`
- 나는 testCode 레포에서 연습으로 진행하고 있기 때문에 따로 하진 않을 것

## Poetry

- Python 프로젝트를 작업할 때 몇 가지 패키지를 다운로드 해야한다.
- Django 또한 다운로드 받아야 하는 패키지이다.
- Python 패키지를 다운로드 하는 방법에는 여러가지가 있지만, 가장 좋은 방법은 poetry를 사용하는 방법이다.

### poetry에 대해서

1. python 패키지를 설치하고 관리할 수 있게 해준다.
2. 이걸 사용해서 Django와 필요한 나머지 패키지를 설치할 것.
3. `https://python-poetry.org/docs/` 이동
4. 설치방법은 두 가지. a: OSX, MacOS, Linux, WSL -> curl 사용. b: Windows PowerShell 사용하는 경우 해당 명령어 사용
5. curl -> `curl -sSL https://install.python-poetry.org | python3 -`

### 가상환경이란

1. 가상 환경은 쉽게 생각해 비눗방울이라고 하면 될 것 같다.
2. 가상 환경은 컴퓨터에 같은 패키지를 다운로드 할 수 있게 해준다.
3. 서로 다른 product에 대해 독립적으로 패키지 설치를 허용한다.
4. 가상환경은 컴퓨터에 다른 폴더로 독립적인 설치 환경을 분리할 수 있다.
5. 전역으로 설치하지 않고 같은 패키지를 다른 버전으로 사용하고 싶기 때문
6. 또는 어떤 라이브러리를 사용하고 있는데, 그게 Django의 특정 버전에선 작동하지 않을 수도 있기 때문

### 새로운 가상환경 구축

1. console에서 `$ poetry` 했을 때 작동 해야한다.
2. `$ poetry init` -> 이 명령어를 실행하면 대화하는 느낌으로 패키지를 만들기 위한 가이드가 나타날 것.
3. pyproject.toml 파일 생성 시 성공 : 우리 방울에 대한 description 이다.

### django 설치

1. `$ conda create -n airbnb python=3.9`
2. `$ conda activate airbnb`
3. `$ poetry add django`
4. poetry.lock 파일도 자동으로 만들어진다. 이 파일은 우리의 코드나 가상환경이 필요로 하는 모든 패키지에 대한 정보를 가지고 있다.
5. 핵심은 poetry는 우리의 코드가 실행될 환경에 대한 정보를 담고 있는 파일을 만들 수 있게 해준다.
6. `poetry.lock` 과 `pyproject.toml` 두 개의 파일을 poetry가 읽어서 파일이 가지고 있는 소프트웨어를 설치할 것

### poetry 가상환경 활성화

- `$ poetry shell`
- poetry 가상환경 비활성화 시 -> `$ exit`

## Start Project

- startproject : 프로젝트를 시작하는 명령어
  - `$ django-admin startproject config .`
- .gitignore 추가

- 이렇게 poetry로 가상환경을 가지고 있고, Django 프로젝트도 만들었다.

# 3. OOP WITH PYTHON

## The 4 Pillars of OOP (객체지향 프로그래밍 OOP 핵심 개념 4개)

- abstract
- encapsulation
- inheritance
- polymorphism

- 객체 지향 프로그래밍이 무엇인지, 사람들에게 어떤 도움이 되고, 왜 유용한 가
- Python에서 `class` 를 만들고 상속을 하고 `constructor`를 작성하는데 익숙해져야 하기 때문이다.

## init

- python을 이용해 OOP 코드를 작성
- class를 만드는 것 부터 시작하여 constuctor 메서드가 python class에서 어떻게 동작하는 지 살펴 볼 것
- constructor 메서드는 class가 생성될 때 호출되는 함수이다.
  - python에는 typescript처럼 constuctor 메서드가 없다.
  - 대신에 `__init__` 이라는 이름의 함수가 있다.
  - 이 함수는 `self`라고 불리는 하나의 인자와 함께 호출될 것.

## self

- `self`는 class를 가리킨다. `self`는 class의 instance를 가리키는 것

## init과 self를 통해 배운 것

1. Python 클래스에 constructor 이름의 메서드가 없다는 것
2. constuctor가 아니라 `__init__` 이라고 불린다.
3. `__init__` 메서드가 `self`와 함께 불린다는 것
4. `self`는 여기 있는 class 자체를 가리킨다.
5. `self`는 TS, JS, Java에서 사용하는 `this` 랑 같은 것 -> python에서 `self`라고 부르는 것
6. python은 private이나 public을 지원하지 않고, type도 지정해주지 않는다. 그래서 문자열인지, 숫자인지 지정해줄 필요가 없다.
7. 가장 중요한 건 class 안에 있는 `모든` 메서드는 self를 가장 첫번째 parameter로 한다는 것

## Inheritance

- python 코드로 상속이 어떻게 구현 되는 가?
- 상속은 객체 지향 프로그래밍에서 매우 중요한 특징이다.
  - 왜냐하면 class를 확장할 수 있도록 코드를 재사용할 수 있게 만들어주기 때문
