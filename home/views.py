from django.shortcuts import render
from news.models import News


# From CI Boutique Ado
def index(request):
    """ A view to return the index page """
    news = News.objects.all().filter(status=1).order_by('-created_on')[:4]
    context = {
        'news': news
    }
    return render(request, 'home/index.html', context)
