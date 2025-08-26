from django.shortcuts import render
from .models import Expirationsystem


def home(request):
    products = Expirationsystem.objects.all()
    return render(request, "expiration/home.html", {"products": products})
