from django.urls import path, include
from .views import home, productos, quienessomos, fundacion, registro, aproducto, lproducto, mproducto, FlorViewSet, eproducto
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('flores', FlorViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('productos/', productos, name="productos"),
    path('fundacion/', fundacion, name="fundacion"),
    path('registro/', registro, name="registro"),
    path('aproducto/', aproducto, name="aproducto"),
    path('lproducto/', lproducto, name="lproducto"),
    path('mproducto/<id>/', mproducto, name="mproducto"),
    path('api/', include(router.urls)),
    path('eproducto/<id>/', eproducto, name="eproducto"),
    path('viewcart/', views.viewcart, name="viewcart"),
    path('addcart/<producto_id>/', views.agregar_producto, name="addcart"),
    path('delcart/<producto_id>/', views.eliminar_producto, name="delcart"),
    path('restarcart/<producto_id>/', views.restar_producto, name="restarcart"),
    path('cleancart/', views.cleancart, name="cleancart"),
    path('procesar_compra/', views.procesar_compra, name="procesar_compra"),
]