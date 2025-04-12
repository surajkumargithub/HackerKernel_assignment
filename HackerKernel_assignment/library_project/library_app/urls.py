from django.urls import path
from .views import (
    AuthorCreateView, BookCreateView, BorrowRecordCreateView,
    AuthorListView, BookListView, BorrowListView, ExportExcelView
)

urlpatterns = [
    path('add-author/', AuthorCreateView.as_view(), name='add-author'),
    path('add-book/', BookCreateView.as_view(), name='add-book'),
    path('add-borrow/', BorrowRecordCreateView.as_view(), name='add-borrow'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('borrows/', BorrowListView.as_view(), name='borrow-list'),
    path('export/', ExportExcelView.as_view(), name='export-excel'),
]
