from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name = 'detail'),
    path('signup/',views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login')

]