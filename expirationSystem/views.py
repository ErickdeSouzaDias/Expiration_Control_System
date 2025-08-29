from datetime import datetime

from .forms import RelatorioForm
from .models import Expirationsystem
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.views import View

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


class ExportarPDFView(View):
    def get(self, request, *args, **kwargs):
        # Criar a resposta HTTP para PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="relatorio{datetime.now()}.pdf"'

        # Criar o PDF
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        # Cabeçalho
        p.setFont("Helvetica-Bold", 16)
        p.drawString(200, height - 50, "Relatório de validade")

        # Cabeçalhos da tabela
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, height - 100, "Código")
        p.drawString(150, height - 100, "Nome")
        p.drawString(350, height - 100, "Validade")

        # Dados
        p.setFont("Helvetica", 10)
        y = height - 120
        produtos = Expirationsystem.objects.all()

        for prod in produtos:
            p.drawString(50, y, str(prod.reference_code))
            p.drawString(150, y, prod.product)
            p.drawString(350, y, prod.expiration_date.strftime("%d/%m/%Y"))
            y -= 20

            # Se a página acabou → cria nova
            if y < 50:
                p.showPage()
                y = height - 50
                p.setFont("Helvetica", 10)

        p.showPage()
        p.save()
        return response

