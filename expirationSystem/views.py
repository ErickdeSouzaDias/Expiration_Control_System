from .forms import RelatorioForm
from .models import Expirationsystem
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HomeListView(ListView):
    model = Expirationsystem
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        # pega os parâmetros enviados via GET
        data_inicial = self.request.GET.get("data_inicial")
        data_final = self.request.GET.get("data_final")

        if data_inicial and data_final:
            queryset = queryset.filter(expiration_date__range=[data_inicial, data_final])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RelatorioForm(self.request.GET or None)
        return context

class HomeCreateView(CreateView):
    model = Expirationsystem
    fields = ["reference_code", "expiration_date", "product", "quantity"]
    success_url = reverse_lazy("homeCreate")

class HomeUpdateView(UpdateView):
    model = Expirationsystem
    fields = ["reference_code", "expiration_date", "product", "quantity"]
    success_url = reverse_lazy("homeList")

class HomeDeleteView(DeleteView):
    model = Expirationsystem
    success_url = reverse_lazy("homeList")

