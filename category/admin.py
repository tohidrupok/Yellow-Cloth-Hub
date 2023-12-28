from django.contrib import admin
from .models import Category , PRODUCT_BY , warranty_period , SELLER , Brand


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name', 'slug')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(PRODUCT_BY, CategoryAdmin)
admin.site.register(warranty_period, CategoryAdmin)
admin.site.register(SELLER, CategoryAdmin)
admin.site.register(Brand, CategoryAdmin)
