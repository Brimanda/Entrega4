from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "stock"]
    list_editable = ["precio"]
    search_fields = ["nombre","stock"]
    list_per_page = 10

admin.site.register(Producto, ProductoAdmin)
