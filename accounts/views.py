from django.shortcuts import render, redirect , get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileUpdateForm 
from .forms import UserReviewForm
from .models import UserReview
from store.models import Product 


# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            return redirect('store')                
    return render(request, 'accounts/register.html', {'form':form})


def profile(request):
    return render(request ,'accounts/dashboard.html')   

def user_login(request): 
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        print(user)
        login(request, user) 
        return redirect('profile')
    
    return render(request ,'accounts/signin.html') 

def user_logout(request):
    logout(request)
    return redirect('login') 


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()           
            return redirect('profile') 
    else:
        form = UserProfileUpdateForm(instance=request.user)

    return render(request, 'accounts/update_profile.html', {'form': form})

def add_user_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = UserReviewForm()
    print(form)
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

    reviews = UserReview.objects.filter(product=product)
    print(product_id )
      
    
    

    context = {'form': form, 'reviews': reviews,}
    return render(request, 'store/product-detail.html', context)