from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Customer, CustomerAdmin)
