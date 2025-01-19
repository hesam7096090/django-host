from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update'),
    path('Change_password/', views.change_password, name='change_password'),
    path('saved/', views.saved, name='saved'),
]
