from django.urls import path, include
from .views import home, productos, quienessomos, fundacion, registro, aproducto, lproducto, mproducto, FlorViewSet, eproducto, enciclopedia
from rest_framework import routers
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register('flores', FlorViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('productos/', productos, name="productos"),
    path('fundacion/', fundacion, name="fundacion"),
    path('registro/', registro, name="registro"),
    path('aproducto/', login_required(aproducto), name="aproducto"),
    path('lproducto/', login_required(lproducto), name="lproducto"),
    path('mproducto/<id>/', login_required(mproducto), name="mproducto"),
    path('api/', include(router.urls)),
    path('eproducto/<id>/', login_required(eproducto), name="eproducto"),
    path('enciclopedia/', enciclopedia, name="enciclopedia")
]