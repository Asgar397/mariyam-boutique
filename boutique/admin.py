from django.contrib import admin
from .models import Service, Gallery, Testimonial, Order

admin.site.register(Order)

admin.site.register(Testimonial)

admin.site.register(Gallery)

admin.site.register(Service)

admin.site.site_header = "Mariyam Boutique Admin"
admin.site.site_title = "Mariyam Boutique Admin"
admin.site.index_title = "Welcome to Admin Panel"