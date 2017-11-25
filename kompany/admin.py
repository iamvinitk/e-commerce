from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportMixin

from kompany.models import Category, Products, Mobiles, Laptops


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_type', )


admin.site.register(Category, CategoryAdmin)


class ProductResource(resources.ModelResource):

    class Meta:
        model = Products
        exclude = ('id', )
        import_id_fields = ('product_id', 'product_name', 'stock', 'price', 'discounted_price', 'image_count')


class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['product_name', 'price', 'stock']
    list_display = ('product_name', 'price', 'stock', 'category_type',)
    resource_class = ProductResource


admin.site.register(Products, ProductAdmin)


class MobileResource(resources.ModelResource):

    class Meta:
        model = Mobiles


class MobileAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['product_id', ]
    list_display = ('product_id', 'product_name', 'price', 'model_name', )
    resource_class = MobileResource


admin.site.register(Mobiles, MobileAdmin)


class LaptopResource(resources.ModelResource):

    class Meta:
        model = Laptops


class LaptopAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['product_id', ]
    list_display = ('product_id', 'product_name', 'price', 'product_category', )
    resource_class = LaptopResource


admin.site.register(Laptops, LaptopAdmin)

