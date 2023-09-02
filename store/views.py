from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category 
from django.core.paginator import Paginator
from django.shortcuts import render, redirect , get_object_or_404
from accounts.forms import UserReviewForm  

from accounts.models import UserReview
 
def store(request, category_slug=None):
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category) 
        page= request.GET.get('page')
        paginator = Paginator(products, 1)
        paged_product = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True)
        paginator = Paginator(products, 2) 
        page= request.GET.get('page')
        paged_product = paginator.get_page(page)
                   
    categories = Category.objects.all() 
    context = {'products': paged_product, 'categories': categories,}
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug) 
    product = get_object_or_404(Product,slug=product_slug)
       
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.product = product
            review.save()
            return redirect('profile') 

    else:
        form = UserReviewForm()
    print('single product ', single_product) 
    
    review = UserReview.objects.all()
    
    return render(request, 'store/product-detail.html', {'product' : single_product, 'form': form ,'reviews':review }) 


def store(request, category_slug=None):
    sort = request.GET.get('sort', 'asc') 
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category)
    else:
        products = Product.objects.filter(is_available=True)

    
    if sort == 'asc':
        products = products.order_by('price')
    elif sort == 'desc':
        products = products.order_by('-price')

    page = request.GET.get('page')
    paginator = Paginator(products, 2)
    paged_products = paginator.get_page(page)

    categories = Category.objects.all()
    context = {'products': paged_products, 'categories': categories, 'sort': sort}
    return render(request, 'store/store.html', context)
