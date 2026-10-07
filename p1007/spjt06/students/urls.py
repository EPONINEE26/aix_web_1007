from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    # url(swrite)로 들어오면 views 파일에서 swrite함수를 찾음 
    path('swrite/', views.swrite, name='swrite'),
]