from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('user/', views.get_user_data, name='get_user_data'),
    path('login_api/', views.login_api, name='login_api'),
    path('register/', views.register, name='register'),
    path('register_api/', views.register_api, name='register_api'),
    path('logout/', views.logout, name='logout')
]
