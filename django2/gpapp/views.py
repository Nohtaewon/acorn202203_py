from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def mainFunc(request):
    return render(request, 'index.html')

class myCallView(TemplateView):
    template_name='callget.html'
    
def insertFunc(request):
    # return render(request, 'insert.html')
    
    # 같은 요청명에 대해 get, post를 구분해서 처리 가능
    if request.method=='GET':
        return render(request, 'insert.html')
    elif request.method=='POST':
        buser=request.POST.get('buser')
        irum=request.POST['irum']
        # buser, irum 으로 뭔가를 하면 된다.
        msg1='부서명:'+buser
        msg2='직원명:'+irum
        context={'msg1':msg1, 'msg2':msg2}
        return render(request, 'show.html', context)
    else:
        print('요청 오류')
'''
def insertFuncOk(request):
    # buser=request.GET.get('buser')
    # irum=request.GET['irum']
    buser=request.POST.get('buser')
    irum=request.POST['irum']
    # buser, irum 으로 뭔가를 하면 된다.
    msg1='부서명:'+buser
    msg2='직원명:'+irum
    context={'msg1':msg1, 'msg2':msg2}
    return render(request, 'show.html', context)
'''