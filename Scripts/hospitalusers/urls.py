from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name='hospitalusers'

urlpatterns=[
    #登录界面
    path('login/',LoginView.as_view(template_name='hospitalusers/login.html'),name='login'),
    #注销
    path('logout/',views.logout_view,name='logout'),
    #注册
    path('register/',views.register,name='register'),

]
