from django.contrib import admin
from table.models import Order

class Orders(admin.ModelAdmin):
    list_display = ('name', 'phone', 'real_estate_agency', 'order_description', 'company', 'order_category', 'deadline')
    list_display_links = ('name', 'company')
    search_fields = ('name', 'company')

admin.site.register(Order, Orders)