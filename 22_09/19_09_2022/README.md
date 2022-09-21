- [0. INTRODUCTION](#0-introduction)
  - [Django study를 통해 배울 것](#django-study---------)
  - [왜 사람들이 Django를 좋아하는 가](#-------django--------)
  - [Flask와 Django의 차이 -> 최소화 vs 극대화](#flask--django------------vs----)
- [1. SET UP](#1-set-up)
  - [python3](#python3)
    - [python3 download](#python3-download)
  - [consist folder](#consist-folder)
  - [Poetry](#poetry)
    - [poetry에 대해서](#poetry-----)
    - [가상환경이란](#------)
    - [새로운 가상환경 구축](#-----------)
    - [django 설치](#django---)
    - [poetry 가상환경 활성화](#poetry---------)
  - [Start Project](#start-project)
- [2. OOP WITH PYTHON](#2-oop-with-python)
  - [The 4 Pillars of OOP (객체지향 프로그래밍 OOP 핵심 개념 4개)](#the-4-pillars-of-oop-------------oop-------4--)
  - [init](#init)
  - [self](#self)
  - [init과 self를 통해 배운 것](#init--self---------)
  - [Inheritance](#inheritance)
  - [Recap](#recap)
  - [underscore 메서드](#underscore----)
- [3. Django Basic](#3-django-basic)
  - [3.1 Runserver](#31-runserver)
    - [Django를 실제 서버에 배포할 때는 서버를 실행할 때 manage.py 말고 다른 걸 사용할 것.](#django--------------------------managepy--------------)
  - [3.1 Migrations](#31-migrations)
    - [데이터베이스는 어디에 있는가?](#----------------)
    - [왜 Django는 django_session 테이블을 찾는가?](#--django--django-session----------)
    - [그럼 어떻게 해당 테이블을 생성할 수 있는가?](#-------------------------)
  - [3.2 Recap](#32-recap)
  - [3.3 Super User](#33-super-user)
  - [3.4 Framework vs Library](#34-framework-vs-library)
  - [3.5 Apps](#35-apps)
- [4. DJANGO APPS](#4-django-apps)
  - [4.0 Models](#40-models)
    - [의문점](#---)
  - [4.1 Migrations](#41-migrations)
    - [migration, migrate 완료 -> house 추가 가능](#migration--migrate-------house------)
  - [4.2 Recap](#42-recap)
  - [4.3 Admin](#43-admin)
    - [str method 설정 (houses/models.py)](#str-method-----houses-modelspy-)
    - [admin 패널에 coulmn들을 구현하는 방법 (houses/admin.py)](#admin-----coulmn------------houses-adminpy-)
  - [4.3 Documentation (장고 공식문서)](#43-documentation----------)
- [5. USER APP](#5-user-app)
  - [5.0 Introduction](#50-introduction)
    - [pylance extension 설치](#pylance-extension---)
  - [black extension 설치](#black-extension---)
  - [5.1 Custom Model](#51-custom-model)
  - [5.2 Custom Field](#52-custom-field)
    - [User 모델을 커스텀할 수 있는 방법](#user-----------------)
  - [5.3 Defaults](#53-defaults)
    - [첫번째 에러](#------)
    - [두번째 에러](#------)
  - [5.4 Custom Admin](#54-custom-admin)
    - [field set ( User 관리자 페이지 커스텀 작업)](#field-set---user----------------)
    - [list_display](#list-display)
    - [기억해야할 점](#-------)
    - [black 사용법](#black----)
  - [5.5 Foreign Keys ( 서로 다른 application의 model들을 어떻게 연결시키는 가)](#55-foreign-keys---------application--model---------------)
    - [데이터베이스에 연결성을 어떻게 표현할 수 있는가?](#---------------------------)
    - [지금까지 생성한 applicaion (users, houses를 연결해보자)](#---------applicaion--users--houses--------)
    - [4번에서 두 가지 옵션이 있다.](#4---------------)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# 0. INTRODUCTION

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

# 1. SET UP

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

# 2. OOP WITH PYTHON

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
  - 왜냐하면 class를 확장할 수 있도록 코드를 재사용할 수 있게 만들어주기 때문\

## Recap

- 속성을 정의할 때만 init 메서드를 사용하면 된다.
- `Django` 굉장히 객체 지향적인 프레임워크이다.
- 굉장히 많은 클래스들을 가지고 있는데, 만약 이것들을 상속 받는다면 ?
  - 여기서 배운 것들을 사용하면 굉장히 많은 시간을 아낄 수 있을 것.
  - 클래스로부터 확장하는 일이 많을 수 있다.
    - 이때 메소드 오버라이딩을 많이 활용할 것.
    - 그리고 가끔 부모 클래스로부터 메서드를 호출할 것.

## underscore 메서드

- ex) `__str__` 메서드

  - init 과 str 뿐만 아니라, 다른 것들은 어떻게 찾는지도 배울 예정

- 이건 굉장히 흥미롭고, 파이썬의 내부가 어떻게 작동하는지 알아보기에 좋다.

- 어떻게 underscore 메서드들을 찾아볼 수 있는가?
  - 문서를 확인해보는 것
  - 다른 방법으로는 클래스의 dir을 출력하는 방법이 있다.
  - dir는 디렉터리를 의미한다. 클래스의 속성들과 메서드들을 보여준다.
    - ex) `dir(class_name)`

# 3. Django Basic

## 3.1 Runserver

- `manage.py` 파일은 Django 프로젝트를 만들 때 자동으로 만들어졌다.
- 파일 안의 코드를 이해할 필요는 없다.
- 단지, `manage.py` 파일이 terminal에서 Django 명령을 실행한다는 것 뿐이다.

### Django를 실제 서버에 배포할 때는 서버를 실행할 때 manage.py 말고 다른 걸 사용할 것.

- 개발 단계에서 vscode로 작업할 때 모든 커맨드를 `manage.py` 를 사용해 실행 할 것.
- `$ python manage.py runserver` 를 했을 때 `db.sqlite3`라는 파일이 생성되었다.
  - 그리고 적용되지않은 migrations이 18개 있다고도 하는데 아직은 정확히 모른다.

## 3.1 Migrations

- `no such table: django_session` 이라는 에러

  - `Django` 는 django_session이라는 테이블을 DB에서 찾고 있지만 실패하여 발생한 에러
  - 하지만 현재 DB는 django_session이란 테이블을 가지고 있지 않다.

### 데이터베이스는 어디에 있는가?

- 서버를 실행했을 때 자동으로 생성된 `db.sqlite3` 파일이다.
- 이 파일이 데이터베이스 파일이다. ( 이 파일을 Django가 바라보고 있다.)
- 해당 파일에서 django_session 이라는 테이블은 찾고 있던 것.

### 왜 Django는 django_session 테이블을 찾는가?

- Django에는 여러가지 기능들이 내장 되어있다.
- 예를 들면, admin 패널인데 이게 작동하기 위해서는 admin유저가 필요하다.
- admin 유저가 작동하기 위해서는 session이 필요하다.
- Django는 admin유저를 위한, admin 세션을 만드려고 했던 것.

### 그럼 어떻게 해당 테이블을 생성할 수 있는가?

- migration을 통해 가능하다.
- migration은 DB의 모양을 변경하고 싶을 때 사용된다.
- 또는 migration은 DB의 state를 수정한다는 의미.
- 아래 명령어를 수행하기 위해서는 먼저 서버를 종료한다.
- ex) `$ python manage.py migrate`
- `$ python manage.py runserver` 한 뒤에 `http://127.0.0.1:8000/admin` 에 접속해보면 이전의 에러가 사라지고 admin 패널이 렌더링 된다.

## 3.2 Recap

- `Django` 는 세션, 비밀번호 등 모든 유저 데이터를 저장하는 곳으로 DB를 사용한다.
- ex) `you have 18 unapplied migration(s).` 와 같은 에러는 DB에 필요한 transformation이 있는데, 아직 적용되지 않았음을 `Django`가 알게 될 때 나타난다.
- 마이그레이션 파일에는 DB의 모양을 변형시키는 Python 코드가 들어있다.
- 위의 에러는 18개의 파일이 있고, 각 파일에 아직 DB에 적용되지 않은 transformation이 있다는 의미이다.
- 정리하자면, 위 메시지는 DB에 적용되지 않은 마이그레이션 파일이 존재할 때 발생되는 에러이다.
- `Django`가 원하는 모양의 DB에서 저장하고 읽어올 수 있도록 DB모양의 상태를 변경하기 위해서 migrate 명령어를 실행하는 것

## 3.3 Super User

- `$ python manage.py createsuperuser`

  ```
  Username (leave blank to use 'bstudent'):
  Email address:
  Password:
  Password (again):
  This password is too short. It must contain at least 8 characters.
  This password is too common.
  This password is entirely numeric.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  ```

- 어드민 로그인 페이지에 위에 입력한 정보로 로그인을 진행하면 된다.

## 3.4 Framework vs Library

- `Django`는 프레임워크이다. 라이브러리와의 차이점을 아는 것이 `Django`가 실제로 어떻게 동작하는지 이해하는데 도움이 될 것.
- 라이브러리는 파이썬에서 내가 비트코인을 위해 사용했던 `bit` 이다.
- 즉, 라이브러리는 개발자가 호출하는 것 이다.

  - 라이브러리를 import해서, 호출(call)하면 된다.
  - 함수, 클래스, 메서드등 무엇이든 원하는 코드를 작성하고 필요한 상황에서 라이브러리를 import해서 라이브러리 코드를 호출한다.

- 하지만, 프레임워크는 다르다. 프레임워크는 호출하지 않는다.
  - 프레임워크가 우리가 쓴 코드를 호출한다.
- 라이브러리 : 개발자가 import해서 호출
- 프레임워크 : 개발자가 쓴 코드를 호출
  - 코드가 작성된 위치를 보고 프레임워크가 해당 코드를 사용
  - ex) `settings.py` 에서 `TIME_ZONE= "UTC"` 해당 부분을 호출해서 사용하듯이 프레임워크가 코드를 호출해서 사용한다.
  - 만약 `TIME_ZONE = "Asia/Seoul"` 로 변경했다면, `Django`가 해당 variable을 보고 스스로 변경된 `TIME_ZONE`으로 초기화 한다.

## 3.5 Apps

- `Django` 프로젝트는 application으로 나누어져있다.
  - 장고의 apps에 관한 개념
- 하나의 어플, 즉 하나의 폴더는 방을 위한 폴더가 될 것.
  - 폴더의 데이터는? -> room 즉 집이 될 것 (airbnb)
  - 즉, 데이터는 집이고 데이터의 조작은 집을 검색하는 것.
  - 집의 편의시설, 집의 룰, 집의 설명등.. 이렇게 데이터 한 조각에 대해서 많은 조작이 수행된다.
- 그래서 user 로직을 위한 파일과, room 로직을 위한 파일을 분리할 것.

  - 데이터도 마찬가지이다. 데이터별로 다른 테이블을 사용할 것.

- 이게 바로 `Django` app이다. 우리의 application의 로직과 데이터를 합쳐서 캡슐화한다.
- `Django` 사용자는 더 잘 정리하기 위해 그것들을 어떻게 분리할지만 정하면 된다.
- application을 모듈을 생각하는 것 처럼 하면 될 것 같다.
- 만약 프로젝트를 한다고하면, 각각 분리 시킬 수 있는 모듈이 무엇일지 고민해봐야한다.
  - 그렇게 별개의 폴더에 캡슐화 하는 것.
- 모듈화는 어플리케이션을 좀 더 정리되게끔 만들어준다.

# 4. DJANGO APPS

## 4.0 Models

- `$ python manage.py startapp houses`
- `Django`는 프레임워크이기 때문에, `houses` 폴더 안의 파일들이 선택사항이 아니라는 의미이다.

  - 이러한 파일들은 꼭 존재해야하고, 장고가 호출해서 쓰기 때문.
  - 그래서 파일에 쓰는 코드는 중요하다.
  - ex) models.py -> 모델은 어플리케이션에서 데이터의 모양을 묘사한 것.
    - 이런 데이터의 설명과 같은 것들은 정확히 우리가 `models.py` 에서 작성해야하는 것듣이다.
    - 그러면 `Django`는 `models.py` 안의 코드를 가져가서 DB에게 말을 건다.

1. House class 만들기 `(houses/models.py)`

- 실제 어플리케이션에서 실제 클론 코딩을 할 때는 집, 경험, 하우스 규칙, 편의시설을 위한 모델, 예약, 유저, 리뷰, 리스트를 위한 모델 등 엄청 많다.
- `TextField`는 `CharField` 보다 길다. `CharField`는 텍스트를 쓰고 싶을 때 쓰는 건데, 길이가 약간 짧거나 문자길이에 제한을 줘야할 때 사용한다.
- `TextField`는 유저가 길이가 긴 텍스트를 쓸 수 있게 해준다.

2. config/settings.py 에서 houses app 설정\

- `INSTALLED_APPS = []` -> 여기에 application을 알려주는 의미다.

### 의문점

- `$ python manage.py startapp houses` 부터 시작해서 reviews, payments.... 모듈화를 시키는 것이라고 이해를 했다.
- 근데 나는 지금까지 하나로만 진행을 해왔는데,, 혼동이 온다.

## 4.1 Migrations

- `Django`에게 왜 이런 식으로 데이터를 설명해야 하는가?

  - DB와 소통해야 하기 때문.
  - DB는 원래 SQL언어로 소통하는데, `Django`가 좋아서 데이터가 어떻게 생겼는지 이해한다.
  - 이걸로 인하여 우리를 대신하여 DB와 소통을 해준다.
  - 즉, 파이썬 코드를 쓰면 `Django`는 그것을 SOL 코드로 번역한다.
  - 그리고 이미 `Django`에게 데이터가 어떻게 생겼는지 설명하고 있기 때문에, DB와 소통하는 것 외에 멋진 것들을 할 수 있는 것.
    - 이미 데이터가 어떻게 생겼는지 알고 있으니 우리 데이터에 대한 관리 패널을 자동으로 생성해주는게 가능하다.
    - 그래서 커스텀 데이터에 대한 관리 패널을 자동으로 생성해준다.

- 객체지향에서는 많은 것들을 상속 받을 수가 있다.

```python
@admin.register(House)
class houseAdmin(admin.ModelAdmin):
    pass
```

- 이렇게 만들어 준 뒤, DB한테 House model에 대해 알려줘야 한다.
  - 그렇지않으면 에러가 발생한다.

1. `$ python manage.py makemigrations`

- 위의 명령어를 실행하면 아래의 결과가 나온다.
  ```
  Migrations for 'houses':
  houses/migrations/0001_initial.py
    - Create model House
  ```

2. 위에서 볼 수 있듯이, Django가 house/migrations 라는 폴더 내부에 파일을 만들었다.

3. migration을 적용시키려면?

- `$ python manage.py migrate`

  ```
  Operations to perform:
  Apply all migrations: admin, auth, contenttypes, houses, sessions
  Running migrations:
  Applying houses.0001_initial... OK
  ```

- models 안의 어떤 데이터의 형태를 수정하든 간에, DB에게 사실을 알려줘야만 한다.
  - 그래서 migration을 생성한 다음, migrate을 하면 된다.

### migration, migrate 완료 -> house 추가 가능

- models에서 정의한 name, price, Description, address들이 추가가 될 수 있다. 새로운 데이터를 직접 만드는 것

## 4.2 Recap

1. application은 데이터와 그 데이터의 로직이 들어있는 섬 같은 것
2. 그래서 처음으로 `House` 를 위한 application을 `$ python manage.py startapp houses`로 만들어주었다.
3. 그리고 `config/setting.py` 에서 application 설정을 해주었다. -> `"houses.apps.HousesConfig"` 를 `INSTALLED_APP = []` 에 추가

4. 만약 새로 생성한 application을 따로 관리하고 싶다면, `CUSTOM_APPS = []` 를 만들어서 안에 넣고, 나머지는 `SYSTEM_APPS =[]` 안에 넣어준다.
5. 그리고 `INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS` 로 해준다.

6. `models.py` 파일이 application에 있는 데이터의 정의나 설명을 적는 곳이다.
7. 그리고 application에서 가지고 있을 데이터를 설명한다.

8. 이 방법이 유용한 이유에는 두 가지가 있다.

- 첫번째 : `Django`가 파이썬 코드로 되어있는 데이터의 형태를 데이터베이스에게 SOL언어로 설명해줌으로 써 데이터베이스와 소통해준다.
- 두번째 : 해당 application 폴더 안에 있는 `admin.py` 파일에서 model을 등록시키기만 해도 `Django`가 admin 패널을 통째로 만들어준다.
  - 검색, 삭제, 편집, 생성까지 가능한 admin 패널이다.

9. 중요한 점은 `models.py` 에서 테이블을 만든 후 에 migration을 생성하지 않고 migrate도 안되어있으면 에러가 발생한다.

- `$ python manage.py makemigrations` 명령어를 통해 `models.py` 안에 무언가 있다는 것을 알게 된다.
- 그리고 나서 `$ python manage.py migrate` 명령어를 통해 생성한 migration을 적용시켜주면 된다.
- 위의 과정들이 수행되면, 데이터베이스의 형태를 업데이트 한다.

## 4.3 Admin

- 프레임워크를 사용하기 때문에, 알맞는 property를 사용하는 것. -> 그러면 `Django`가 알아서 해준다.
- 여기서, 프레임워크만 사용하게 되면 프레임워크 없이는 뭘 해야 할지 모르게 되는 문제가 발생한다.
  - 프레임워크를 위한 코드를 짤 줄 밖에 모른다. 실제로 `Django`를 쓰면 일어나는 일이다.
  - 만약 Python으로 프로그래밍 하는 법을 먼저 배우지 않고 장고부터 한다면, 이런 참조만 할 줄 알게 된다는 것.

### str method 설정 (houses/models.py)

- 아래의 코드를 넣어주면 admin 패널에서 깔끔하게 확인할 수 있다.

  ```
      def __str__(self):
          return self.name
  ```

### admin 패널에 coulmn들을 구현하는 방법 (houses/admin.py)

- `list_display`라는 property이다.

  ```python
  @admin.register(House)
  class houseAdmin(admin.ModelAdmin):
    # pass
    list_display = [
        "name",
        "price",
        "addreess",
        "pets_allowed"
    ]
  ```

## 4.3 Documentation (장고 공식문서)

- `https://www.webforefront.com/django/modeldatatypesandvalidation.html`

- `https://docs.djangoproject.com/ko/4.1/ref/models/fields/`

# 5. USER APP

## 5.0 Introduction

- user applicaion을 만들고 그 안에서 user model, User class를 만들 것.
- 그리고 AbstractUser 라는 걸 모두 상속 받을 것.

### pylance extension 설치

- vsCode를 위한 python 서버이다.
- 자동완성, 자동 import 같은 걸로 날 도와줄 수 있다

## black extension 설치

- `$ poetry add --dev black --allow-prereleases`

## 5.1 Custom Model

- 새로운 application users 생성
- `AbstractUser` 상속 - users/models.py
- `setting.py` -> app추가, AUTHMODEL 추가
- 서버 종료
- `db.sqlite3` 파일 삭제
- houses migrations 파일 1~3 삭제
- makemigrations, migrate
- 서버 재실행
  ```python
  python manage.py startapp users
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver-
  ```
- userAdmin 적용 - `admin.py`

  ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    @admin.register(User)
    class CustomUserAdmin(admin.ModelAdmin):
        pass
  ```

## 5.2 Custom Field

- 5.1에서 우리만의 User 모델을 가지고 있게 되었다. 하지만 커스텀은 되어있지 않다.
- 5.2에서 커스텀을 해볼 것.

### User 모델을 커스텀할 수 있는 방법

- AbstractUser를 덮어쓴다
- 속성 몇 개를 없앤다
- 로직을 추가한다

## 5.3 Defaults

### 첫번째 에러

- `It is impossible to add a non-nullable field 'is_host' to user without specifying a default. This is because the database needs something to populate existing rows.Please select a fix` 해당 에러가 발생한 이유
  - `non-nullable field` 때문인데, 이건 무엇인가?
  - `BooleanField`는 두 개만 될 수 있다. (True or False)
  - 그렇기 때문에, null이 될 수 없다.
- 에러 해결에는 두가지 옵션이 있다.
  - 첫번쨰 : default 값을 추가하는 것
    - 만약 `default=False` 옵션을 주면 이전에 생성된 모든 사용자는 해당 column 값을 False로 받게된다.
  - 두번째 : `null=True` 옵션을 주는 것
    - 그러면 `Django`가 여기엔 아무값을 넣지않으면서 이 column을 추가할 수 있다.

### 두번째 에러

- `It is impossible to add a non-nullable field 'name' to user without specifying a default. This is because the database needs something to populate existing rows.Please select a fix:`
  - 기존에 이미 생성된 사용자에게는 어떤 값을 부여해야하는지에 대한 에러
  - `default = ""` 로 해결

## 5.4 Custom Admin

### field set ( User 관리자 페이지 커스텀 작업)

- 관리자 페이지에서 model의 field가 보이는 순서를 설정할 수 있게 해준다
- 일종의 섹션 안에 field를 넣어서 그 섹션에 제목을 붙일 수 있다는 것

- field와 field set의 차이점
  - 섹션을 추가할 수 있다.

### list_display

- 사용자 list를 표시할 때 보이는 column을 설정하는 Tuple이다.

### 기억해야할 점

- fieldsets나 list_display에 넣은 필드가 꼭 model안에 존재해야한다는 것

### black 사용법

- 자동 formatting 되게 설정하려고 했는데, 적용이 되질 않는다.
- 그래서 black이 설치는 되어있으니 `$ black admin.py` 이렇게 명령어로 format을 수정해주고 있다.

## 5.5 Foreign Keys ( 서로 다른 application의 model들을 어떻게 연결시키는 가)

```
예를 들어 house에 호스트(주인)가 있었으면 좋은 상황,
그리고 그 주인은 Users model 안에 있는 사용자가 되어야한다.
이게 바로 '연결' 이 필요한 이유이다.
인스타그램에선 사용자가 사진을 올릴 수 있다. 이 말은 사진에는 업로드한 사람이 있다는 것.
사용자는 댓글을 달 수 있다. 그 댓글은 사진에 달린 것. 사용자는 사진에 좋아요를 할 수 있고
좋아요는 사진이랑 연결되어 있다. 이렇게 모든 게 연결되어 있다.

airbnb의 경우에는 house에 주인이 있다. 그리고 house에는 사용자로부터 작성된 리뷰가 있다.
그리고 사용자는 house도 만들 수 있다.
사용자 간의 메시지를 주고 받을 수 있는 채팅방도 있다. (두 사람이 한 채팅방에 있다)
채팅방에는 사용자로부터 작성된 메시지가 있다.

그래서 model을 연결하는 방법을 꼭 알아야 한다.
```

### 데이터베이스에 연결성을 어떻게 표현할 수 있는가?

- `Django` 랑 데이터베이스는 기본적으로 unique한 ID를 데이터베이스에 있는 모든 object에 만들고 있다.
- 그래서 원하든 원하지않든 데이터베이스에 생성한 모든 것들은 ID를 가지고 있다.(PK와 같은 의미 == Primary Key 기본키)
- 생성하고 이전의 ID를 지우더라도 ID는 다시 사용되지 않는다.

### 지금까지 생성한 applicaion (users, houses를 연결해보자)

1. 사용자에 대한 정보를 저장하는 User 테이블 (AbstractUser)
2. 집에 대한 정보를 저장하는 House 테이블
   - 테이블에 owner column 추가 한 뒤, 유저의 ID를 넣을 것.
   - 이를 통해서 house에 사용자의 ID를 저장할 수 있는 column이 owner인 것을 알 수 있다.
3. 단순한 숫자가 아니기 때문에 , owner column의 타입은 양의 정수가 아니다.
   - `Foregin Key(외래키)` 이다.
   - 외래키로 column의 타입을 정해주면, `Django`는 이 숫자가 User 테이블에 있는 user의 ID라는 것을 알게 된다.
   - 나중에 room 정보를 가져올 때, `Django`는 이 숫자도 가져와서 숫자 2인 ID를 가진 사용자를 찾은 후
   - 해당 사용자에 대한 정보를 함께 줄 것이다.
4. `models.ForeignKey()`로 타입을 지정해준 뒤, 어떤 model의 것을 저장하는 건지 알려줘야한다.
   - `models.ForeignKey("users.User")` ----------------> `"users.User" == "application_name.DB_name"`
   - `TypeError: __init__() missing 2 required positional arguments: 'to' and 'on_delete'` : 에러
   - Foreign Key도 필수 요소로 on_delete가 필요하다
   - `on_delete`는 참조하는 model이 삭제될 때 어떻게 할건지를 설정하게 해준다.

### 4번에서 두 가지 옵션이 있다.

1. 주인이 계정을 지워도 주인이 설정하지 않은 house를 가지고 싶다면 -> `on_delete=models.SET_NULL`

- 이렇게 하면 사용자가 계정을 지워도 house는 주인이 없는 상태로 남을 것

2. 만약 그렇지 않다면 -> `on_delete=models.CASCADE` 를 하면 된다.

- `CASCADE`의 의미는 사용자가 계정을 지우면 house도 지워진다는 의미이다.

5. 모두 완료 되었다면, migrations , migrate을 하면 된다.

- 필요한 default 값을 지정하는게 귀찮으면 `migrations` 폴더의 기록들과 `db.sqlite3` 을 지워주면 된다.
