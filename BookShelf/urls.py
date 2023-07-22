from django.urls import path
from . import views


urlpatterns = [
    path('add_book_api/', views.add_book_api, name='add_book_api'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book_api/<int:book_id>', views.update_book_api, name='update_book_api'),
    path('update_book/<int:book_id>', views.update_book, name='update_book'),
    path('delete_book_api/<int:book_id>', views.delete_book_api, name='delete_book_api'),
]
