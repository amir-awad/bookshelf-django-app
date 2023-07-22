"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Authors import views as authors_views
from BookShelf import views as bookshelf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authors_views.login, name='login'),
    path('login/', authors_views.login, name='login'),
    path('login_api/', authors_views.login_api, name='login_api'),
    path('logout/', authors_views.logout, name='logout'),
    path('register/', authors_views.register, name='register'),
    path('register_api/', authors_views.register_api, name='register_api'),
    path('add_book/', bookshelf_views.add_book, name='add_book'),
    path('add_book_api/', bookshelf_views.add_book_api, name='add_book_api'),
    path('update_book_api/<int:book_id>', bookshelf_views.update_book_api, name='update_book_api'),
    path('update_book/<int:book_id>', bookshelf_views.update_book, name='update_book'),
    path('delete_book_api/<int:book_id>', bookshelf_views.delete_book_api, name='delete_book_api'),
]