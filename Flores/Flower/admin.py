from django.contrib import admin
from .models import Producto
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Producto)

admin.site.register(User, UserAdmin)




