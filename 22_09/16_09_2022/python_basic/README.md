- 파이썬에서 변수명을 작성할 때 가장 많이 쓰이는 방법은 `_` 를 이용하는 것 ( snake Case )

---

### data type

- boolean

  - True
  - False

- string

  - `""`

- number

---

### example code

```
my_name = "hun"
age = 26
dead = False

print("Hi my name is" , my_name)
print("and I'm ", age, "years old")
```

---

### functiom

- 함수의 정의는 `def` 라는 단어를 이용해 `function` 을 정의할 수 있다.

  - ex)

        ```
        def say_hello():
          print("hello")

        say_hello()
        ```

- 파이썬에서 빈 공백은 코드에 영향을 끼치는 아주 중요한 요소이다.
- 파이썬은 빈 공백을 이용해 어떤 것 안에 들어있는지 이해하기 때문

  - 이렇게 함으로써 파이썬을 아주 가독성 좋게 만들어준다.
  - 다른 프로그래밍 언어들은 빈 공백을 신경쓰지 않는다.

    - Java, JS, C#, TypeScript, Rust, Go 등 다른 언어들도 이런규칙을 가지고 있지 않아서 항상 중괄호 `({})` 를 써야한다.
    - 함수에서 함수를 쓰고싶으면 아래 처럼 사용하면 된다.

      ```
      def say_bye():
      print("bye bye")
      say_hello()
      ```

---

- 출력결과를 수정하거나 바꾸기 위해 `function` 에 어떻게 데이터를 보내면 되는가

```
def say_hello(user_name):
   print("hello", user_name, "how are you?")

say_hello("hun")

# output
hello hun how are you?

```

- 이렇게 하면 코드를 재사용할 뿐만 아니라 출력결과도 변경할 수 있게 된다.
- 보다시피, 이제 직접 데이터를 `function`에 넣고 `function`은 이 데이터를 받아서 사용한다.

### 프로그래머들이 이런 것들을 언급할 때 사용하는 용어들

- `user_name` 과 같은 것은 `parameter` 라고 한다. 또는 `parameter`
  - 함수로 전달하는 데이터를 저장하기 위한 `placeholder(그릇)` 의 의미를 가지고 있다.
- `say_hello("hun")` 처럼 실제로 전달한 데이터는 `argument` 라고 한다.

---

- print 함수에 `(데이터, 데이터, 데이터, ...)` 이렇게 할 수 있는 것 처럼 예제 함수에서도 같은 걸 하고싶다.

  - 해야 할 건, parameter 에서 `def say_hello(user_name, user_age):` 이렇게 추가해주면 된다. -> 2개의 데이터를 위한 공간이 생김
  - 한 개의 데이터만 argument만 넣는다면, 필수 argument가 없다는 에러가 발생한다. 왜냐하면 `say_hello()`는 2개의 데이터를 받는다고 정의했기 때문
    - 데이터를 넣는 순서도 중요하다. 첫번째 argument는 첫번째 parameter에 저장되며 마찬가지로 두번째 argument도 두번째 parameter에 저장된다.
  - 또 기억해야할 점은 `call` 한다는 것은 괄호 쓰는 걸 의미한다. 마치 실행버튼을 누르는 거랑 마찬가지 `ex) say_hello("hun", 12)`

---

- 함수는 우릴 더 생산적인 개발자로 만들어준다.
- 함수란, 작성해서 몇번이고 재사용이 가능한 코드
- parameter란, 함수 안으로 데이터를 보내 함수의 결과를 바꿀 수 있게 해주는 것

- 함수에 있어서 매우 유용한 한 가지

  - argument로 데이터를 함수의 parameter로 보내주지 않으면 에러가 발생하는데, 이때 parameter의 기본값을 설정해주면 에러가 나지 않는다.
  - 사용자가 parameter 없이 함수를 호출하는 경우를 관리해주기 위함

- ex)

```
def say_hello(user_name="anonymous"):
    print("hello", user_name)

say_hello("hun")
# output -> hello hun

say_hello()
# output -> hello anonymous
```

---

### return 키워드

- 함수에 대해 생각하는 방식을 바꿀 것이기 때문에 매우 중요
- 함수 내에서 무언가를 출력하는 것 뿐만 아니라 함수로부터 값을 받는 것도 가능하다.

  - 이렇게 하면 코드를 보고, 생각하고, 함수에 대해 생각하는 방식을 바꾸게 될 것

- 코드 밖에서 특정 함수의 결과를 받아서 나중에 코드에서 사용하고 싶다면?
  - 먼저 함수에서 무언가를 받아오는 법을 알아야 한다.
  - 함수는 주스 기계라고 생각하면 되고, 데이터를 과일이라고 생각하면
    - 주스기계(함수)에 과일(데이터)를 넣으면 과일주스를 얻을 수 있다.
    - 이 방식이 `return 키워드` 가 하는 역할이다.

---

### while

- while을 사용하는 코드는 유용하다.
  - 무언가를 계속 실행하게 해주기 때문이다.
  - 물론 멈추게 할 수도 있다.

```
distance = 0

while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1

```

---

### data structure ( 자료구조 ) 를 사용하여 데이터 구조화에 대해 알아보기

배워야할 파이썬의 자료구조는 3가지가 있다.

- 첫번째: list
- 두번째: tuple
- 세번째: dictionary

- data structure ( 자료구조 )는 무엇일까?
  - 데이터를 구조화하고 싶을 때 사용하는 것

### list

- 일주일의 모든 요일을 목록으로 만드는 것
- list는 variable 한 개 안에 모든 데이터를 넣을 수 있어야 한다.
- list 안에 데이터를 넣을 때는 쉼표를 사용해서 데이터를 분리한다.

- method 데이터 뒤에 결헙/연결된 function 이다.
  - ex) name = 'hun'
  - print(name.upper())
  - output -> HUN
