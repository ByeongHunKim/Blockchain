# 목차

- [Chapter6 : MODELS AND ADMIN](#chapter6---models-and-admin)
  - [6.0 User Model](#60-user-model)
    - [column 추가](#column---)
    - [column 옵션 만드는 방법](#column----------)
    - [Pillow 패키지](#pillow----)
    - [Pillow 설치](#pillow---)
  - [6.1 Room Model](#61-room-model)
    - [새로운 application 만들기](#----application----)
    - [새로운 model 만들기](#----model----)
    - [해당 model에 amenity 라는 새로운 model 만들기](#---model--amenity--------model----)
  - [6.2 Many to Many](#62-many-to-many)
    - [many to one <-> one to many 의 의미](#many-to-one-----one-to-many-----)
    - [many to many](#many-to-many)
    - [many to many 질문](#many-to-many---)
    - [amenity 적용 방법 ( models.py )](#amenity---------modelspy--)
    - [created_at = models.DateTimeField(auto_now_add=True) 의 의미](#created-at---modelsdatetimefield-auto-now-add-true------)
    - [updated_at = models.DateTimeField(auto_now=True) 의 의미](#updated-at---modelsdatetimefield-auto-now-true------)
    - [모두가 공유 가능한 공통 코드를 가지고 있을 application 만들기](#-------------------------application----)
    - [abstract 사용하는 방법](#abstract--------)

# Chapter6 : MODELS AND ADMIN

## 6.0 User Model

### column 추가

- profile_photo
  - `Django`는 `Imagefield`가 있다.
- gender
  - 유저의 성별

### column 옵션 만드는 방법

- 가끔은 아무 텍스트나 넣는게 아니라 관리자 페이지에서 옵션을 선택 하기를 원할 수 있기 때문.
- 그래서 user 클래스 안에 또 다른 class를 만들면 된다.

- 예시

```python
    # column에 옵션 추가하는 방법
    class GenderChoices(models.TextChoices):
        # 이 튜플에는 DB에 들어갈 value, 관리자 페이지에서 보게 될 label이 들어간다.
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    # 그리고 gender column에 옵션 추가
    gender = models.CharField(max_length=10, choices=GenderChoices)


```

- `$ python manage.py makemigrations`
- `$ python manage.py migrate`
- `$ python manage.py runserver`

- user의 `admin.py` 에 새로 만든 필드를 추가해줘야 관리자페이지에서 볼 수 있다.

  - 관리자 페이지는 시각화를 제공한다.

- form에서 특정 column을 필수가 아니게 하려면 `models.py` 에서 `blank=True`로 해주면 된다.

### Pillow 패키지

- Python에서 이미지를 가지고 작업할 수 있게 해준다.

### Pillow 설치

- pip가 아니라 poetry를 사용하고 있기 때문에 에러에 나온 명령어(pip)로 설치하면 안된다.
- `$ poetry add Pillow`

  ```
  Using version ^9.2.0 for Pillow

  Updating dependencies
  Resolving dependencies... (0.1s)

  Writing lock file

  Package operations: 1 install, 0 updates, 0 removals

  • Installing pillow (9.2.0)
  ```

## 6.1 Room Model

### 새로운 application 만들기

- `$ python manage.py startapp rooms`

- `config/setting.py` 에서 applicaion 추가하기

### 새로운 model 만들기

- `rooms/models.py` 에서 model 추가하기

- `""" Room Model Definition """` 이라는 코드 컨벤션이 있다.

### 해당 model에 amenity 라는 새로운 model 만들기

- amenity란?
  - many-to-many 관계 ( 다대다 관계 )

## 6.2 Many to Many

### many to one <-> one to many 의 의미

- 이 둘은 거의 비슷한데, 어느 것에서부터 보느냐에 따라 다르다.
- ex) room은 여러 개다. 1,2,3번 방 모두 같은 owner를 가질 수 있다.

  - 즉 user가 여러 room을 만들 수 있다.
  - 이게 바로 `many to one` 관계이다.

- 위의 상황을 뒤집으면 `one to many` 관계와 같다.

  - 한 user가 여러 room을 가질 수 있다.

- keypoint : room의 owner와 한 user의 모든 room에 어떻게 접근하는가?

### many to many

- `amenity model`이 `many to many` 관계를 사용해야하기 때문.
- `many to many` 관계는 우리가 `amenity`와 같이 많은 것을 가질 수 있다는 것
- 이 경우에는 하나의 room이 여러 `amenity` 를 가질 수 있다

  - 그리고 여러 `amenity`들이 여러 room에서 사용할 수 있다

- ex) 예를 들어 많은 room들은 부엌을 가지고 있을 것 이다.

  - 그리고 부엌은 여러 방에 있을 수 있다.

- keypoint : many to many 관계는 여러 `amenity` 들이 여러 room 안에 있을 수 있도록 해준다는 것

### many to many 질문

- 그러면 먼저 amenity에 해당하는 옵션들? 을 먼저 설정하고 room 별로 존재하는 옵션을 넣는 구조로 이해했다.

### amenity 적용 방법 ( models.py )

- room Class에서 각 room이 여러 `amenity`를 가질 수 있다고 나타내기 위해 column을 추가한다.
- data type은 `ManyToManyField` 로 지정해주고, 어떤 model을 가지고 싶은지 적어줘야한다.
  - 그 model은 rooms application 안에 Amenty model이 될 것

### created_at = models.DateTimeField(auto_now_add=True) 의 의미

- 필드의 값을 해당 object가 처음 생성되었을 때 시간으로 설정한다.
- 무슨의미냐면, room이 만들어지면 `Django` 는 이 방이 만들어진 date를 이 부분에 넣는 다는 뜻

  - 어 그러면 tx field도.. ? 트랜잭션이 발생하면 object가 하나 생성될텐데, 굳이 timeStamp값을 추출하지 않아도 되는 것 아닌가?

- 또한 이것이 언제 업데이트 되었는지도 알고 싶다.

### updated_at = models.DateTimeField(auto_now=True) 의 의미

- `auto_now_add` 와 `auto_now` 와는 서로 다르다.
- `auto_now`는 object가 저장될 때마다 해당 필드를 현재 date로 설정하는 것.
  - 이건 매우 중요하다
  - `auto_now_add` property는 처음 생성 되었을 때 채워질 것이다.
  - `auto_now` 는 room을 업데이트 할 때마다 설정 될 것이다.
- 근데 문제는 이것들을 복사해서 아래에 붙여넣기 때문에 발생한다.
  - 많은 model을 만들 때 이걸 복붙해야한다면 좋지 않다.
  - 시간을 아끼기 위해서는 다른 application을 만들어야한다.
  - 그건 다른 application과 공유할 수 있는 코드를 갖게 될 것

### 모두가 공유 가능한 공통 코드를 가지고 있을 application 만들기

- `$ python manage.py startapp common`
- `config/setting.py`에 추가하기
- `common/models.py` 에서 abstract model 만들기

  - 여기서 만들려고하는 model은 데이터베이스에 추가하지 않을 model이다.
  - 다른 model에서 재사용하기 위한 model이다
  - 따라서 이건 model을 위한 설계도 같은거다

  ```python
  class CommonModel(models.Model):

    """ Common Model Definition """

    # 중복되는 2개의 field를 가질 예정
    # Django에게 이 model이 DB에 보여지지 않기를 바란다고 말해야한다.
    # 이 모델이 다른 model들이 설계도로 사용하는 model이 되기를 원한다.
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    # 이 class는 Django에서 model을 configure 할 때 사용한다.
    # abstact로 되어있으면, model을 봐도 저장하지 않는다. -> 다른 application에서 재사용 가능
    class Meta:
        abstract = True
  ```

### abstract 사용하는 방법

- abstract의 의미는 이 model이 데이터베이스에서 실제 데이터로 사용되지 않을 거라는 뜻이다.

  - abstract가 true라고 하면 이 코드를 재사용하기 위해 사용한다고 말하는 것

- abstract를 설정해준 model을 사용하고자 하는 model에서 import 해야한다.

  ```python
  from common.models import CommonModel

  class Room(CommonModel):
  ```

- 적용한뒤 makemigrations, migrate을 하면 끝

## 6.3 Recap

- model 이 abstract 라는 건, Django가 model을 데이터베이스에 넣지 않기를 바란다는 뜻
  - 대신 이 model을 설계도로 사용하겠다는 것

### rooms/admin.py admin 패널

-

## 6.4 Rooms Admin

### 어떻게 python에게 class를 string으로 보여줄 수 있을까?

- 장고 모델을 포함한 모든 class에는 메서드를 사용하여 class가 string으로 보이게 하도록 할 수 있다.
  - str method
  ```python
      def __str__(self) -> str:
        return self.name
  ```
  - admin.py 에서 list_filter에 created_at, updated_at 을 쓰면 오늘, 지난7일, 이번달, 이번해 등으로 filter할 수 있다.
  - 그렇지 않고 , models.py 에서 `readonly_fields = ()` 안에 넣으면 특정 column을 눌렀을 때 안에서도 확인이 가능하다.
