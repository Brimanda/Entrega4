from email import message
from django.shortcuts import redirect, render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProductoForm
from .models import Producto, Flor
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .carro import Carro
from rest_framework import viewsets
from .serializers import FlorSerializer
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

class FlorViewSet(viewsets.ModelViewSet):

    queryset = Flor.objects.all()
    serializer_class = FlorSerializer


def home(request):

    return render(request, 'core/home.html')

def quienessomos(request):

    return render(request, 'core/quienessomos.html')

def productos(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/productos.html', data)

def fundacion(request):

    return render(request, 'core/fundacion.html')

def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def aproducto(request):

    data = {

        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
            return redirect(to="lproducto")
        else:
            data["form"] = formulario

    return render(request, 'admin/aproducto.html', data)

def lproducto(request):

    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {

        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'admin/lproducto.html', data)

def mproducto(request, idProducto):
    
    producto = get_object_or_404(Producto, idProducto = idProducto)

    data = {

       'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance= producto, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lproducto")
        data["form"] = formulario

    return render(request, 'admin/mproducto.html', data)

def eproducto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    producto.delete()
    return redirect(to="lproducto")




