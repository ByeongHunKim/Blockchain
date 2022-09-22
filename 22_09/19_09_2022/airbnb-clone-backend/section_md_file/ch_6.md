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
