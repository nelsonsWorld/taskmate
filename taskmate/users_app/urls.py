from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', views.register, name = 'register'),
   # You can create a folder "registration" if you want to use 
   # the default directory for your login/logout templates
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name= 'login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('logout1', views.logout1, name = 'logout1'),
]
