from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cart
from .models import CartProducts
from .utils import get_or_create_cart
from Flower.models import Producto

def cart(request):

    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
       'cart': cart
    })

def add(request):

    cart = get_or_create_cart(request)

    product = Producto.objects.get(pk=request.POST.get('product_id'))
    
    quantity = int(request.POST.get('cantidad', 1))

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)

    return render(request, 'carts/add.html', {
        'product': product
    })

def remove(request):
    cart = get_or_create_cart(request)

    product = Producto.objects.get(pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')
