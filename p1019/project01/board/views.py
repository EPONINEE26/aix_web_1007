from django.shortcuts import render

def blist(request):
    return render(request, 'blist.html')

# GET : 페이지 열기, POST : 저장
def bwrite(request):
    if request.method=="GET":    
        return render(request, 'bwrite.html')
    elif request.method=="POST":
        btitle = request.POST.get('btitle')
        id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print(f'데이터확인 : {btitle},{id},{bcontent},{bfile}')
        return render(request, 'bwrite.html')

def bview(request):
    
        return render(request, 'bview.html')