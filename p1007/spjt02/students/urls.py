
from django.urls import path, include
from.import views # students 내 view를 찾아감. 같은 폴더 내에는 .을 입력

urlpatterns = [
    path('s_write/', views.s_write),  
]

