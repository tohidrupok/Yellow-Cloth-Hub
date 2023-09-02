from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart , CartItem
# Create your views here.
def cart(requrst):
    session_id = requrst.session.session_key 
    cartid = Cart.objects.get(cart_id = session_id)
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    cart_items = None
    if cart_id: 
        cart_items = CartItem.objects.filter(cart = cartid)
                       
    return render(requrst, 'cart/cart.html', {'cart_items':cart_items} ) 

def add_to_cart(request ,product_id ):
    product = Product.objects.get( id = product_id)   
    print(product)  
    session_id = request.session.session_key 
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    if cart_id:        
        cart_item = CartItem.objects.filter(product = product).exists()
        if cart_item:
            item = CartItem.objects.get(product = product)
            item.quantity += 1
            item.save()
        else:
            cartid = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
                cart = cartid ,
                product = product,
                quantity = 1
            )
            item.save()
        
    else:
        cart = Cart.objects.create(
        cart_id = session_id )
        cart.save() 
        
      
    return redirect('cart')
    