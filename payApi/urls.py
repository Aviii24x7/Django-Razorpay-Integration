from django.urls import path
from payApi import views

urlpatterns = [
    path('', views.home, name="home"),
    path('success',views.success,name="success")
]
