from django.http import HttpResponse

def home(request):
    return HttpResponse("Mariyam Boutique is Live 🚀")

from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username="asgar").exists():
        User.objects.create_superuser("asgar", "asgar@email.com", "Asgar@123")
        return HttpResponse("Superuser created")
    return HttpResponse("Already exists")