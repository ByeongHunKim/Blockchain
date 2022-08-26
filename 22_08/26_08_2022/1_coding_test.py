# 문제 ------------------------------------------------------------------------------
# 유저가 회원가입 페이지에서 입력한 이메일과 비밀번호의 값을 받은 상황이다.
# SignUp 이라는 데이터베이스 테이블에 접근해서 이미 존재하는 유저인지 유효성 검사를 하려고한다.
# SignUp 테이블에서 기존 유저들의 이메일 정보는 username 이라는 컬럼에 저장되어있다.
# 'value' : '1' = 회원가입이 완료되었을 때
# 'value' : '0' = 데이터베이스에 이미 존재하는 이메일 주소 일 때  

@csrf_exempt
def signup(request):
    try:
        # axios data 받는 것--------------------------------------------
        data = json.loads(request.body.decode('utf-8'))
        userEmail = data['username']
        password = data['password']
        # -------------------------------------------------------------
        userCount = SignUp.objects.filter().count()
        if:
            new_user = SignUp.objects.create_user(**form.cleaned_data)
            context = {'value':'1'}
            return HttpResponse(json.dumps(context))
        else:
            context = {'value':'0'}
            return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))


# 정답 ------------------------------------------------------------------------------
@csrf_exempt
def signup(request):
    try:
        # axios data 받는 것--------------------------------------------
        data = json.loads(request.body.decode('utf-8'))
        print('data: ', data)
        form = signUpForm(data)
        userEmail = data['username']
        password = data['password']
        # -------------------------------------------------------------
        userCount = SignUp.objects.filter(username = userEmail).count()
        isValidUser = form.is_valid()
        if isValidUser == True : # 또는 userCount == 0
            new_user = SignUp.objects.create_user(**form.cleaned_data) # 유저생성
            context = {'value':'1'}
            return HttpResponse(json.dumps(context))
        else:
            print("이미존재하는 유저")
            context = {'value':'0'}
            return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))