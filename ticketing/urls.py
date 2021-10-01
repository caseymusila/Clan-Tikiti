from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/',views.registerPage, name='register')
    path('home/',views.home, name='home'),
    path('create_event/', views.create_event, name='create_event'),
    path('disp_event/<project_id>',views.disp_event, name='disp_event')
]