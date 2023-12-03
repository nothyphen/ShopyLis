from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login_page'),
    path('register/', views.register, name='register_page'),
    path('verify/', views.verify, name='verify_page'),
    path('logout/', views.logout, name='logout_page'),
    path('forget/', views.forgetpassword, name='forgetpassword_page'),
    path('account/', views.account, name='account_page'),
    path('change/', views.changepassword, name='change_page'),
]