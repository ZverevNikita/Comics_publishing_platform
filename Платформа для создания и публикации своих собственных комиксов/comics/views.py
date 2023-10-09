from django.http import Http404
from django.shortcuts import render

from comics.models import ComicBook


def comic_list(request):
    comics = ComicBook.objects.filter(publish=True)

    return render(request, 'index.html', {'comics': comics})


def comic_detail(request, pk):
    comic: ComicBook = ComicBook.objects.filter(pk=pk).first()
    if comic is None:
        raise Http404()

    pages = comic.comicbookpage_set.all().order_by('id')

    return render(request, 'comic-detail.html', {'comic': comic, 'pages': pages})
