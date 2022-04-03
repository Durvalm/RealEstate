from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('property/<str:type>/', views.property, name='property'),

]

