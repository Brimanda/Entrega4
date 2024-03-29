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
    path('mproducto/<idProducto>/', mproducto, name="mproducto"),
    path('api/', include(router.urls)),
    path('eproducto/<idProducto>/', eproducto, name="eproducto"),
]