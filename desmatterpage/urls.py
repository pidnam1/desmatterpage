"""desmatterpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from blog import views as blog_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('signup/', blog_views.signup, name='signup'),
    path('signup/company',blog_views.company_signup, name = 'company_signup'),
    path('signup/manufacturer', blog_views.manufacturer_signup, name = 'manufacturer_signup'),
    path('blog/', blog_views.index, name = 'index'),
    path('blog/detail/', blog_views.detail, name= 'detail'),
    path('reset/',
        auth_views.PasswordResetView.as_view(
        template_name='blog/password_reset.html',
        email_template_name='blog/password_reset_email.html',
        subject_template_name='blog/password_reset_subject.txt'
    ), name = 'password_reset'),
    path('reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),
    name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='blog/password_change.html'),
    name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='blog/password_change_done.html'),
    name='password_change_done'),
    path('blog/profile', blog_views.myProfile, name = 'profile'),
    path('blog/projects', blog_views.projects, name = 'projects'),
    path('blog/orders', blog_views.orders, name = 'orders'),
    path('blog/payments', blog_views.payments, name = 'payments'),
    path('blog/products', blog_views.products, name = 'products')
]
