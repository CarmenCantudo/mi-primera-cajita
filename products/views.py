from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm

from django.http import HttpResponse


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    from Code Institute Boutique Ado
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    from Code Institute Boutique Ado
    """
    print('----------------------')
    product = get_object_or_404(Product, pk=product_id)
    print('----------------------')
    return HttpResponse(product)
    print('----------------------')
    add_favourite = False
    reviews = ProductReview.objects.filter(product_id=product.id).order_by('-created_on')  # noqa
    ratings = ProductReview.objects.all().aggregate(Avg('rating'))
    total_reviews = reviews.count()

    if product.favourites.filter(id=request.user.id).exists():
        add_favourite = True

    context = {
        'product': product,
        'add_favourite': add_favourite,
        'reviews': reviews,
        'ratings': ratings,
        'total_reviews': total_reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    from Code Institute Boutique Ado
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    from CI Boutique Ado
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    from CI Boutique Ado
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a product review """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            data = ProductReview()
            data.review = form.cleaned_data['review']
            data.rating = form.cleaned_data['rating']
            data.product = product
            data.user_id = request.user.id
            data.save()
            messages.success(request,
                             'Review sent for approval!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           "Sorry your review could not be submitted.")
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductReviewForm()

    template = 'products/product_detail.html'

    return render(request, template)


def edit_review(request, review_id):
    """ Edit a product review """
    review = get_object_or_404(ProductReview, id=review_id)
    product = review.product

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has being successfully \
                             updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Your review couldn\'t be updated. \
                            Please ensure the form is valid.'
                           )
    else:
        form = ProductReviewForm(instance=review)
        messages.info(request, 'You are editing your review')

    template = 'products/edit_review.html'

    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id, ):
    """ Delete a product review """
    review = get_object_or_404(ProductReview, id=review_id)

    if request.user == review.user:
        review.delete()
        messages.success(request, 'Review deleted!')

        return redirect('product_detail', review.product.id)
    else:
        messages.error(
            request,
            'Failed to delete review. Please ensure that you have permission.')

    return redirect('product_detail', review.product.id)
