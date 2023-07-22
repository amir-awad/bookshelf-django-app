from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from BookShelf.models import Book

@api_view(['POST'])
def add_book_api(request):
    book = Book.objects.create(
        name=request.data['book-name'],
        description=request.data['book-description']
    )
    book.save()

    authors_names = request.data['book-authors'].split(',')
    authors = User.objects.filter(username__in=authors_names)
    book.author.set(authors)
    
    return Response({
        "book_info": {
            "name": book.name,
            "description": book.description,
        }
    })
    
def add_book(request):
  if(request.session.get('username')):
    return render(request, 'add_book.html')

  return render(request, 'login.html')


@api_view(['POST'])
def update_book_api(request, book_id):
    book = Book.objects.get(id=book_id)
    book.name = request.data['book-name']
    book.description = request.data['book-description']
    book.save()

    authors_names = request.data['book-authors'].split(',')
    authors = User.objects.filter(username__in=authors_names)
    book.author.set(authors)
    
    return Response({
        "book_info": {
            "name": book.name,
            "description": book.description,
        }
    })
    
def update_book(request, book_id):
  if(request.session.get('username')):
    book = Book.objects.get(id=book_id)
    return render(request, 'update_delete_book.html', {'book': book})

  return render(request, 'login.html')

@api_view(['POST'])
def delete_book_api(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    
    return Response({
        "book_info": {
            "name": book.name,
            "description": book.description,
        }
    })
