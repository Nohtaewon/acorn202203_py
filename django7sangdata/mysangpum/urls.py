from django.urls import path
from mysangpum import views 

urlpatterns = [
     
    path('list', views.ListFunc),
    path('insert', views.InsertFunc), 
    path('insertOk', views.InsertOkFunc), 
    path('update', views.UpdateFunc),
    path('updateOk', views.UpdateOkFunc), 
    path('delete', views.DeleteFunc),
]