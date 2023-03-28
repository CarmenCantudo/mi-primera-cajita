from django.contrib import admin
from .models import Product, Category, ProductReview
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'available',
        'quantity',
    )
    search_fields = (
        'sku',
        'name',
        'category',
        'available',
    )
    ordering = ('sku',)
    list_filter = ('available', 'quantity',)
    summernote_fields = ('description',)
    actions = ['available', 'not_available']

    def available(self, request, queryset):
        queryset.update(available=True)

    def not_available(self, request, queryset):
        queryset.update(available=False)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """Review Admin"""
    list_display = (
        'product',
        'user',
        'review',
        'rating',
        'created_on',
        'approved',
    )

    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ReviewAdmin)
