from django import forms

class RelatorioForm(forms.Form):
    data_inicial = forms.DateField(
        label="Data inicial",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_final = forms.DateField(
        label="Data final",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
