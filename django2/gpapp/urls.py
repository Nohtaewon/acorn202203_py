from django.urls import path
from gpapp import views

urlpatterns = [
    path('insert', views.insertFunc),
    # path('insertok', views.insertFuncOk),
]