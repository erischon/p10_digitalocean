from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('mentions/', views.mentions, name='mentions'),
]
