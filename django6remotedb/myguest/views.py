from django.shortcuts import render, redirect
from myguest.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SelectFunc(request):
    
    print(Guest.objects.filter(title__contains="안녕"))
    print(Guest.objects.get(id=1))
    print(Guest.objects.filter(id=1))
    print(Guest.objects.filter(title='연습'))
    
    # 정렬
    gdata=Guest.objects.all()
    # gdata=Guest.objects.all().order_by('title')     # 제목별 오름차순      
    # gdata=Guest.objects.all().order_by('-title')    # 제목별 내림차순
    # gdata=Guest.objects.all().order_by('-title', 'id')
    # gdata=Guest.objects.all().order_by('-id')[0:2]
    
    return render(request, 'list.html', {'gdata':gdata})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        Guest(
            title=request.POST['title'],
            content=request.POST['content'],
            # regdate=datetime.now()
            regdate=timezone.now()
        ).save()
        # print(request.POST.get('title'))
        
    # return HttpResponseRedirect('/guest/select')     # 추가 후 목록 보기. redirect 방식으로 요청
    return redirect('/guest/select')