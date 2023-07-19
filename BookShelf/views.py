from django.shortcuts import render

books = [
  {
    "book_name": "To Kill a Mockingbird",
    "book_author": "Harper Lee",
    "book_description": "A classic novel set in the American South, dealing with racial injustice and moral growth.",
    'date_posted': 'July 18, 2023'
  },
  {
    "book_name": "1984",
    "book_author": "George Orwell",
    "book_description": "A dystopian novel set in a totalitarian society, exploring themes of government control and surveillance.",
    'date_posted': 'July 18, 2023'
  },
  {
    "book_name": "The Great Gatsby",
    "book_author": "F. Scott Fitzgerald",
    "book_description": "A story of the Jazz Age, portraying the decadence and excess of the Roaring Twenties.",
    'date_posted': 'July 18, 2023'
  },
  {
    "book_name": "Pride and Prejudice",
    "book_author": "Jane Austen",
    "book_description": "A romantic novel set in the early 19th century, focusing on the themes of love, marriage, and social status.",
    'date_posted': 'July 18, 2023'
  },
  {
    "book_name": "The Hobbit",
    "book_author": "J.R.R. Tolkien",
    "book_description": "An epic fantasy novel following the journey of Bilbo Baggins and his adventures with dwarves and dragons.",
    'date_posted': 'July 18, 2023'
  }
]

def home(request):
    context = {
        'books': books
    }
    return render(request, './index.html', context)
