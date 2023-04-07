from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News


class NewsAdmin(SummernoteModelAdmin):
    """ Manage News in the admin panel """
    list_display = ('title', 'slug', 'status', 'created_on', 'image')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    actions = ['publish_articles']

    def publish_articles(self, request, queryset):
        queryset.update(status='1')


admin.site.register(News, NewsAdmin)
