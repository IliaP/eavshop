from django.contrib import admin
from shop.models import Product
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

class ProductAdminForm(BaseDynamicEntityForm):
    model = Product

class ProductAdmin(BaseEntityAdmin):
    form = ProductAdminForm

admin.site.register(Product,ProductAdmin)

