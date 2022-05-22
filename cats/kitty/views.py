from django.shortcuts import get_object_or_404, render

from .models import Cat


def index(request):
    return render(request, 'kitty/index.html', {'all_cats': Cat.objects.all()})


def detail(request, cat_slug):
    return render(request, 'kitty/detail.html', {'cat': Cat.objects.get(slug=cat_slug)})
