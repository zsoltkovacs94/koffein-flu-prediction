from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gen', views.gen, name="gen"),
    path('tan', views.tan, name="tan")
]
