from django.urls import path
from btrapp import views

urlpatterns = [
    path('',views.registration,name='registeration'),
    path('login',views.userlogin,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.profile,name="profile"),
    path('update',views.update,name='update'),
]