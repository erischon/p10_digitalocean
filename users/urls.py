from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('moncompte/', views.moncompte, name='moncompte'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('myproducts/', views.myproducts, name='myproducts'),
    path('myproducts_delete/<int:product>',
         views.myproducts_delete, name='myproducts_delete'),
    # Password
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
]
