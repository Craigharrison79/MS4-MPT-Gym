from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductReview
from .forms import ProductReviewForm

from .forms import ProductForm


# Create your views here.
def all_products(request):
    """
    To return a view to the different services.
    """

    categories = Category.objects.all()
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

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    To return a view to see a single service details.
    """

    product = get_object_or_404(Product, pk=product_id)
    # for the product review rating post
    form = ProductReviewForm()

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only Gym Owner can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Faild to add product. \
                 Please ensure the form is valid.')
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
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only Gym Owner can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is vaild.')
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
    Delete a product from the store.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only Gym Owner can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Allow users to add  a product review """

    product = get_object_or_404(Product, pk=product_id)

    # https://stackoverflow.com/questions/56982579/how-to-display-all-the-reviews-for-the-particular-product

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Your review \
                    has been successfully added!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Something went wrong! \
                    Please try to add your review again.')
    context = {
        'form': form
    }
    return render(request, context)


@login_required
def delete_review(request, review_id):
    """ Delete review """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry,just site managment can do that.')
        return redirect(reverse('home'))
    elif request.user.is_superuser:
        # https://stackoverflow.com/questions/70024172/how-to-delete-model-by-filtering-with-pk
        review = ProductReview.objects.filter(pk=review_id).last()
        # need the product id
        product_id = review.product_id
        review.delete()
        messages.success(request, f"{ review.user }'s review '{ review.comment }' has been \
        removed!")
        return redirect(reverse('product_detail', args=[product_id]))
