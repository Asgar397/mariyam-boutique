from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
from django.shortcuts import render
from .models import Service
from .models import Gallery
from .models import Testimonial
from .models import Customer
import openai
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Order

def payment(request):
    return render(request, "payment.html")

def create_order(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        design = request.POST.get("design")

        order = Order()
        order.name = name
        order.phone = phone
        order.design = design
        order.amount = 10000
        order.save()

    return redirect("/payment/")

def ai_chat(request):
    question = request.GET.get("q")

    answer = "Our boutique provides custom stitching services."

    return JsonResponse({"reply": answer})

def home(request):
    gallery = Gallery.objects.all()
    testimonials = Testimonial.objects.all()

    return render(request, "home.html", {
        "gallery": gallery,
        "testimonials": testimonials
    })


def about(request):
    return render(request, "about.html")

def services(request):
    services = Service.objects.all()
    return render(request, 
    "services.html", {"services": services})
@api_view(['GET'])
def single_customer(request, id):

    customer = Customer.objects.get(id=id)
    serializer = CustomerSerializer(customer)

    return Response(serializer.data)

@api_view(['GET','POST'])
def get_customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(['DELETE'])
def delete_customer(request, id):

    customer = Customer.objects.get(id=id)
    customer.delete()

    return Response("Customer deleted successfully")

@api_view(['PUT'])
def update_customer(request, id):

    customer = Customer.objects.get(id=id)
    serializer = CustomerSerializer(customer, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)