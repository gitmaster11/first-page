
from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'image_tag']
    list_display_links = ('name',)
    list_filter = ('name',)
    list_editable = ('price',)
    search_fields = ('name',)
    readonly_fields = ('image_tag',)
    list_per_page = 10
    search_help_text = "Qidirayotgan mahsulotingiz nomini kiriting"
    save_as = True

    def image_tag(self, obj):
        return format_html('<img style="width:30%; height:30%" src="{}" />'.format(obj.image))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'image_tag']
    list_display_links = ('name',)
    list_filter = ('created_to',)
    list_editable = ('is_active',)
    search_fields = ('name', 'slug')
    readonly_fields = ('image_tag',)
    list_per_page = 10
    search_help_text = "Qidirayotgan mahsulotingiz nomini yoki slugini kiriting"

    def image_tag(self, obj):
        return format_html('<img style="width:40%; height:40%" src="{}" />'.format(obj.image))

admin.site.register(Order)
admin.site.register(OrderProduct)
