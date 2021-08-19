from django.shortcuts import render
from book.forms import PostSearchForm
from book.models import Book


def post_search(request):
  form = PostSearchForm

  results = []

  if 'q' in request.GET:
    form = PostSearchForm(request.GET)
    if form.is_valid():
      q = form.cleaned_data['q']
      
      results = Book.objects.filter(title__contains=q)

  return render(request, 'index.html', {'form':form, 'results':results})
