from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SobModel, SearchModel, Book
from django.db.models import Q

# Create your views here.


class SobList(ListView):
    template_name = "home.html"
    model = SobModel


class SearchList(ListView):
    template_name = "search.html"
    model = SobModel


class BookList(ListView):
    template_name = "book_list.html"
    model = SobModel

    def get_queryset(self):
        q_word = self.request.GET.get("query")

        if q_word:
            object_list = SobModel.objects.filter(
                Q(title__icontains=q_word) | Q(memo__icontains=q_word)
            )
        else:
            object_list = SobModel.objects.all()

        return object_list
