from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("customers/", views.get_customers, name="get_Customers"),
    path('customers/<int:id>/', views.single_customer),
    path('customers/update/<int:id>/', views.update_customer),
    path('customers/delete/<int:id>/', views.delete_customer),
]