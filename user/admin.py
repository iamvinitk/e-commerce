from django.contrib import admin

# Register your models here.
from user.models import Cart, Orders, Addressbook


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(Cart, CartAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', )


admin.site.register(Orders, OrdersAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'house_number', 'country', )


admin.site.register(Addressbook, AddressAdmin)
