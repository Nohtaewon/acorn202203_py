from django.shortcuts import render

# Create your views here.

def mainFunc(request):
    name="홍길동"
    return render(request, "main.html", {'msg':name})
