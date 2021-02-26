from django.urls import path, include
from .views import SobList, SearchList, BookList

urlpatterns = [
    path("home/", SobList.as_view(), name="hame"),
    path("search/", SearchList.as_view(), name="search"),
    path("book/", BookList.as_view(), name="book"),
]
