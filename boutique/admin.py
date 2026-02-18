from django.contrib import admin
from .models import Service, Customer

admin.site.register(Service)
admin.site.register(Customer)

admin.site.site_header = "Mariyam Boutique Admin"
admin.site.site_title = "Mariyam Boutique Admin"
admin.site.index_title = "Welcome to Admin Panel"