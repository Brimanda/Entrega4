from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from .models import ShippingAddress
from .forms import ShippingAddressForm

from Carts.utils import get_or_create_cart
from Orders.utils import get_or_create_order

# Create your views here.

class ShippingAddressListView(LoginRequiredMixin, ListView):
    
    login_url = 'login'
    model = ShippingAddress
    template_name = 'addresses/addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')

class ShippingAddressUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'addresses/update.html'

    def get_success_url(self):
        return reverse('Address:addresses')

class ShippingAddressDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'addresses/delete.html'
    success_url = reverse_lazy('Address:addresses')


@login_required(login_url='login')
def create(request):

    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists() 

        shipping_address.save()

        if request.GET.get('next'):
            if request.GET['next'] == reverse('orders:address'):
                cart = get_or_create_cart(request)
                order = get_or_create_order(cart, request)

                order.update_shipping_address(shipping_address)

                return HttpResponseRedirect(request.GET['next'])

        messages.success(request, 'Direccion registrada correctamente')
        return redirect(to='Address:addresses')

    return render(request, 'addresses/create.html', {
       'form': form 
    })

@login_required(login_url='login')
def default(request, pk):

    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('Carts:cart')

    if request.user.has_shipping_address:
        request.user.shipping_address.update_default()

    shipping_address.update_default(True)

    return redirect('Address:addresses')