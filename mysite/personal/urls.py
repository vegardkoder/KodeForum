from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('LogoutView', views.LogoutView, name='LogoutView'),
    path('rules', views.Rules, name="rules"),
    path('profile/edit/', views.edit_profile, name='edit_profile')
]
