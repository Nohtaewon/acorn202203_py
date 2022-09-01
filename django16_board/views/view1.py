from django.shortcuts import render
from myboard.models import BoardTab
def mainFunc(request):
    aa = "<div><h2>메인화면</h2></div>"
    return render(request, 'main.html', {'main':aa})

def listFunc(request):
    data_all = BoardTab.objects.all().order_by('-id')
    datas = data_all
    
    return render(request, 'board.html', {'datas':datas})

def insertFunc(request):
    pass

def insertokFunc(request):
    pass

def searchFunc(request):
    pass

def contentFunc(request):
    pass

def updateFunc(request):
    pass

def updateokFunc(request):
    pass

def deleteFunc(request):
    pass

def deleteokFunc(request):
    pass
