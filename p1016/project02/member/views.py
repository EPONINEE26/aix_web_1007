from django.shortcuts import render,redirect

def login(request):
    if request.method=="GET":
        return render(request, 'login.html')

    elif request.method=="POST":
        
        return render(request, 'login.html')










def logout(request):
    return render(request, 'login.html')



def mwrite(request):
    return render(request, 'mwrite.html')






def mupdate(request):
    return redirect('/')