from django.db import models

class Board(models.Model):
    # bno = 게시판번호
    # id = 회원아이디
    # btitle : 제목, bcontent : 내용
    # 답변달기 
    # bgroup-답변달기 그룹핑, bstep-그룹순서, bindent-들여쓰기 
    # bhit: 조회수
    # bdate : 게시글 등록일 
    # bfile : 파일첨부   
    
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=30) 
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField() # 대용량 text 
    
    # 답변달기
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    bhit = models.IntegerField(default=1)
    bdate = models.DateTimeField(auto_now=True,blank=True)
    bfile = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.bno},{self.id},{self.btitle},{self.bcontent},{self.bstep},{self.bindent},{self.bhit},{self.bdate},{self.bfile}'

