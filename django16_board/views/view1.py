from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.http.response import HttpResponseRedirect
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def mainFunc(request):
    aa = "<div><h2>메인화면</h2></div>"
    return render(request, 'main.html', {'main':aa})

def listFunc(request):
    # data_all = BoardTab.objects.all().order_by('-id')
    # datas = data_all
    
    data_all = BoardTab.objects.all().order_by('-id')
    per_page = 10
    paginator = Paginator(data_all, per_page)
    page = request.GET.get('page')
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
    
    return render(request, 'board.html', {'datas':datas})

def insertFunc(request):
    return render(request, 'insert.html')

def insertokFunc(request):
    if request.method == 'POST':
        # print(request.POST.get('name'))
        try:
            gbun = 1    # Group number 구하기
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id + 1
                
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],  # request.META.get('REMOTE_ADDR')
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0,
                
            ).save()
            
        except Exception as e:
            print('추가 에러 : ', e)
            return render(request, 'error.html')
    
    return HttpResponseRedirect('/board/list')  # 추가 후 목록보기
    # return redirect('/board/list')

def searchFunc(request):    # 검색용
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        # print(s_type, s_value)
        
        # SQL의 like연산과 유사한 칼럼명__contains=값
        if s_type == 'title':
            datas_search = BoardTab.objects.filter(title__contains=s_value).order_by('-id')
        elif s_type == 'name':
            datas_search = BoardTab.objects.filter(name__contains=s_value).order_by('-id')
            
        per_page = 10
        paginator = Paginator(datas_search, per_page)
        page = request.GET.get('page')
        try:
            datas = paginator.page(page)
        except PageNotAnInteger:
            datas = paginator.page(1)
        except EmptyPage:
            datas = paginator.page(paginator.num_pages)
        
        return render(request, 'board.html', {'datas':datas})
    
def contentFunc(request):
    page = request.GET.get('page')
    data = BoardTab.objects.get(id=request.GET.get('id'))
    # 조회수 갱신
    data.readcnt = data.readcnt + 1
    data.save()
    return render(request, 'content.html', {'data_one':data, 'page':page})
    
def updateFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print('수정자료 읽기 오류 :', e)
        return render(request, 'error.html')
    
    return render(request, 'update.html', {'data_one':data})

def updateokFunc(request):
    try:
        upRec = BoardTab.objects.get(id=request.POST.get('id'))
        
        if upRec.passwd == request.POST.get('up_passwd'):   # 비밀번호 비교
            upRec.name = request.POST.get('name')
            upRec.mail = request.POST.get('mail')
            upRec.title = request.POST.get('title')
            upRec.cont = request.POST.get('cont')
            upRec.save()
        else:
            return render(request, 'update.html', {'data_one':upRec, 'msg':'비밀번호 불일치!'})
        
    except Exception as e:
        print('수정 처리 오류 :', e)
        return render(request, 'error.html')
     
    return redirect('/board/list')      # 수정 후 목록보기

def deleteFunc(request):
    try:
        delData = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print('삭제자료 읽기 오류 :', e)
        return render(request, 'error.html')
    
    return render(request, 'delete.html', {'data_one':delData})

def deleteokFunc(request):
    delData = BoardTab.objects.get(id=request.POST.get('id'))
    
    if delData.passwd == request.POST.get('del_passwd'):
        delData.delete()
        return redirect('/board/list')  # 삭제 후 목록보기
    else:
        return render(request, 'error.html')    # 비밀번호가 틀린 경우 등
