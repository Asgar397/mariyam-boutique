from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")
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