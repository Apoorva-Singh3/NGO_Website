

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('backend/', views.backend, name='backend'),

    path('login/', views.Login, name='login'),
    path('login_user', views.LoginUser, name='login_user'),
    path('logout/', views.LogoutUser, name='logout'),
]
