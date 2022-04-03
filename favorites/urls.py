from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorites, name='favorites'),
    path('add_fav/<int:id>/', views.add_fav, name='add_fav'),
    path('remove_fav/<int:id>/', views.remove_fav, name='remove_fav'),

]