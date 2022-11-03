from django.contrib import admin

from .models import ProductInBasket


# Register your models here.
class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]


admin.site.register(ProductInBasket, ProductInBasketAdmin)
