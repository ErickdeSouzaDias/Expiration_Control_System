from .models import Expirationsystem
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class HomeListView(ListView):
    model = Expirationsystem

class HomeCreateView(CreateView):
    model = Expirationsystem
    fields = ["reference_code", "expiration_date", "product", "quantity"]
    success_url = reverse_lazy("homeCreate")