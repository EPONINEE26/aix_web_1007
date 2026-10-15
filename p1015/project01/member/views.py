from django.shortcuts import render
from member.models import Member

# GET, POST 
def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        try:
            qs = Member.objects.get(id=id,pw=pw) # , : and의 의미 # db에 회원 존재 확인
            # session 추가 
            request.session['session_id'] = qs.id
            request.session['session_nickname'] = qs.nickname
            context = {'temp':1}
        except Member.DoesNotExist:
            context = {'temp':0}
            
        print(f'로그인정보 : {id},{pw} / 회원확인 : {context}')
        # context 파이썬에서 html 로 보낼 수 있는 데이터 
        # python => html : context
        # html => python : form, url path, 파라미터, 자바스크립트(ajax)
        return render(request, 'login.html', context) # context 파이썬에서 html 로 보낼 수 있는 데이터 
    

    
    
    
def step01(request):
    return render(request, 'step01.html')

def step02(request):
    return render(request, 'step02.html')

def step03(request):
    return render(request, 'step03.html')

def step04(request):
    return render(request, 'step04.html')