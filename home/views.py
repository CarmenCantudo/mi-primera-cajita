from django.shortcuts import render


# From CI Boutique Ado
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
