from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F,Q 
from django.conf import settings
from django.conf.urls.static import static
import os
from member.models import Member


# 게시글 리스트 
def blist(request):
    qs = Board.objects.all().order_by('-bgroup','bstep')
    context = {'list':qs} # id가 memeber로 저장됨. 
    return render(request, 'blist.html',context)

# GET : 페이지 열기, POST : 저장
def bwrite(request):
    if request.method=="GET":    
        return render(request, 'bwrite.html')
    elif request.method=="POST":
        btitle = request.POST.get('btitle')
        # id = request.POST.get('id')
        id = request.session['session_id']
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        print(f'데이터확인 : {btitle},{id},{bcontent},{bfile}')
        
        # create 방식 - member 객체를 저장
        member = Member.objects.get(id=id)
        qs = Board.objects.create(btitle=btitle,member=member,bcontent=bcontent,bfile=bfile)        

        #답변달기
        qs.bgroup = qs.bno
        qs.save()
        
        # save 방식
        # Board(btitle=btitle,id=id,bcontent=bcontent,bfile=bfile).save()
        context = {'temp':1}
        return render(request, 'bwrite.html',context)
            # return redirect('/board/blist/')

# 게시글 상세보기 
def bview(request,bno):
    # board 1개 검색 
    qs = Board.objects.get(bno=bno)
    # qs.bhit = qs.bhit+1
    # qs.save()
    
    # 데이터 1개 가져오기
    qs = Board.objects.filter(bno=bno).first() # .first()
    # qs = Board.objects.filter(bno=bno)
    
    # 조회수 증가     
    # qs.update(bhit=F('bhit')+1) # F함수 : qs에 있는 컬럼값을 가져올 때 사용 
    qs.bhit = qs.bhit+1
    qs.save()   
    
    
    # # 이전글 : -bgroup, bsetp으로 그룹지어진 상태임.
    # pre_qs = Board.objects.filter(bno__lt=bno).order_by('-bno').first()
    # # 다음글 
    # next_qs = Board.objects.filter(bno__gt=bno).order_by('bno').first()
    # 이전글 : -bgroup, bsetp으로 그룹지어진 상태임. / Q함수 or 를 사용할 때 적용
    
    # 답변달기가 있는 경우
    pre_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep) |\
                Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by('-bgroup','bstep').first()
    next_qs = Board.objects.filter(Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep) |\
                Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by('-bgroup','bstep').first()     
    
    context = {'board':qs,'pre_board':pre_qs, 'next_board':next_qs}
    return render(request, 'bview.html',context)

# 게시글 삭제
def bdelete(request,bno):
    # Board.objects.get(bno=bno).delete()
    qs = Board.objects.get(bno=bno)

    # 파일삭제 c:/upload/board/1.jpg
    media_root = settings.MEDIA_ROOT
    remove_file = media_root+"/"+str(qs.bfile)
    if os.path.isfile(remove_file):
        os.remove(remove_file)

    # db삭제
    qs.delete()

    context={'temp':0,'bno':bno}
    return render(request, 'bwrite.html',context)

# 게시글 수정 
# GET : 수정페이지열기, POST:수정저장 
def bupdate(request,bno): 
    if request.method=="GET":
        qs = Board.objects.get(bno=bno) 
        context = {'board':qs}       
        return render(request, 'bupdate.html',context)
    
    elif request.method=="POST":
        btitle = request.POST.get('btitle')
        # id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        # old_file = request.POST.get('old_file')
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.id = id
        qs.bcontent = bcontent
        if bfile:
            qs.bfile = bfile

        qs.save()
        
        context = {'temp':2, 'bno':bno}
        return render(request, 'bwrite.html',context)
    
# 답변달기
def breply(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'breply.html',context)
        