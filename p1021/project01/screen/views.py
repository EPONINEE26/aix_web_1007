from django.shortcuts import render


# 차트그래프
def chart(request):    
    return render(request,'s_chart.html')

def chart_data(request):    
    return render(request,'s_chart.html')