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
      
    # 1.0.1 Standard textual queries (case sensitive)
      # results = Book.objects.filter(title__contains=q)
      # print(Book.objects.filter(title__contains=q).explain(verbose=True, analyze=True))
      # print(Book.objects.filter(title__contains=q).query)

    # # 1.0.2 Standard textual queries (case insensitive)      
      # results = Book.objects.filter(title__icontains=q)
        
    # 1.0.3 Full text search
      # results = Book.objects.filter(title__search=q)

    # 1.0.4 SearchVector (search against multiple fields)
      # from django.contrib.postgres.search import SearchVector
      # results = Book.objects.annotate(search=SearchVector('title', 'authors'),).filter(search=q)  

    # 1.0.5 Search Ranking
      # from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
      # vector = SearchVector('title', weight='A') + SearchVector('authors', weight='B')
      # query = SearchQuery(q)
      # results = Book.objects.annotate(rank=SearchRank(vector, query, cover_density=True)).order_by('-rank')

    # 1.0.6 Search TrigramSimilarity & TrigramDistance
      # from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
      # results = Book.objects.annotate(similarity=TrigramSimilarity('title', q),).filter(similarity__gte=0.3).order_by('-similarity')
      # results = Book.objects.annotate(distance=TrigramDistance('title', q),).filter(distance__lte=0.8).order_by('distance')

    # 1.0.7 Search Headline
      # from django.contrib.postgres.search import SearchHeadline, SearchQuery, SearchVector
      # query = SearchQuery(q)
      # vector = SearchVector('authors')
      # results = Book.objects.annotate(search=vector, headline=SearchHeadline('authors', query, start_sel='<span>', stop_sel='</span>', )).filter(search=query)

      from django.contrib.postgres.search import TrigramSimilarity

      print("#1")
      print(Book.objects.filter(title__trigram_similar=q).explain(analyze=True))
      print("#2")
      print(Book.objects.filter(title__trigram_similar=q).annotate(similar=TrigramSimilarity('title', q)).order_by('-similar').explain(analyze=True))


  return render(request, 'index.html', {'form':form, 'results':results, 'q':q})
