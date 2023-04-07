from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import News
from .forms import NewsForm


def news(request):
    """
    All News Articles
    """
    news = News.objects.all().filter(status=1)
    template = 'news/news.html'
    context = {
        'news': news
    }
    return render(request, template, context)


@login_required
def add_news(request):
    """
    Add a News Article
    """
    if request.method == "POST":
        form = NewsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Your article was added successfully!")
            return redirect(reverse('news_details', args=[obj.slug]))
        else:
            messages.error(
                request, "Failed to add article, please check if the form is \
                    valid")
    else:
        form = NewsForm()

    template = 'news/add_news.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def news_details(request, slug):
    """
    Full News Article
    """
    context = {}
    news = News.objects.get(slug=slug)

    context['news'] = news

    template = 'news/news_details.html'
    context = {
        'news': news,
    }

    return render(request, template, context)


@login_required
def edit_news(request, slug):
    """
    Edit a News Article
    """
    news = News.objects.get(slug=slug)
    user = request.user

    if request.method == "POST":
        form = NewsForm(request.POST or None,
                        request.FILES or None, instance=news)
        if user == news.author:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                news = obj
                messages.success(request, "Your article was edited \
                                 successfully!")
                return redirect(reverse('news_details', args=[obj.slug]))
            else:
                messages.error(request, "Failed to update article.")
        else:
            messages.info(request, 'You are not allowed to do that. You are \
                not the article author!')
    else:
        form = NewsForm(instance=news)
        messages.info(request, f'You are editing {news.title}')

    template = 'news/edit_news.html'
    context = {
        'news': news,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_news(request, slug):
    """
    Delete a News Article
    """
    news = News.objects.get(slug=slug)
    user = request.user
    if news.author == user:
        news.delete()
        messages.success(request, f'You have deleted {news.title}')
        return redirect(reverse('news'))
    else:
        messages.error(request, "Unable to delete the article.")

    template = 'news/delete_news.html'
    context = {
        'news': news,
    }

    return render(request, template, context)
