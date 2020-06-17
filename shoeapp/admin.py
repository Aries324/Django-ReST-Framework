from django.contrib import admin
from shoeapp.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Register your models here.


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')


admin.site.register(Manufacturer, ManufacturerAdmin)


class ShoeTypeAdmin(admin.ModelAdmin):
    list_display = ('style',)


admin.site.register(ShoeType, ShoeTypeAdmin)


class ShoeColorAdmin(admin.ModelAdmin):
    list_display = ('shoe_colors',)


admin.site.register(ShoeColor, ShoeColorAdmin)


class ShoeAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'brand_name',
        'manufacturer',
        'color',
        'material',
        'shoe_type',
        'fasten_type'
    )


admin.site.register(Shoe, ShoeAdmin)