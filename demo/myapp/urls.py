from  django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register_user/',views.register_user,name='register_user'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('user/',views.userpage,name='userpage'),

]
