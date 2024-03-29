from django.shortcuts import render, get_object_or_404, redirect
from Carts.utils import get_or_create_cart, destroy_cart
from .models import Order
from Address.models import ShippingAddress
from .utils import get_or_create_order, breadcrumb
from .utils import destroy_order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import EmptyQuerySet
from django.views.generic.list import ListView

# Create your views here.

class OrderListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return self.request.user.orders_completed()

@login_required(login_url='login')
def order(request):

    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, 'orders/order.html',{
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })

@login_required(login_url = 'login')
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count() > 1

    return render(request, 'orders/address.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'can_choose_address': can_choose_address,
        'breadcrumb': breadcrumb(address=True)
    })

@login_required(login_url = 'login')
def select_address(request):

    shipping_address = request.user.shippingaddress_set.all()

    return render(request, 'orders/select_address.html', {
       'breadcrumb': breadcrumb(address=True),
       'shipping_address': shipping_address
    })

@login_required(login_url = 'login')
def check_address(request, pk):

    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('Carts:cart')

    order.update_shipping_address(shipping_address)

    return redirect('orders:address')

@login_required(login_url = 'login')
def confirm(request):

    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = order.shipping_address
    if shipping_address is None:
        return redirect('orders:address')
    
    return render(request, 'orders/confirm.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb': breadcrumb(address=True, confirmation=True)
    })

@login_required(login_url='login')
def cancel(request):

    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    if request.user.id != order.user_id:
        return redirect('Carts:cart')

    order.cancel()

    destroy_cart(request)
    destroy_order(request)

    messages.error(request, 'Orden cancelada')
    return redirect('home')

@login_required(login_url='login')
def complete(request):

    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    if request.user.id != order.user_id:
        return redirect('Carts:cart')

    order.complete()

    destroy_cart(request)
    destroy_order(request)

    messages.success(request, 'Compra completada exitosamente')
    return redirect('home')