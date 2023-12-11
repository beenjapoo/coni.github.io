from django import forms
from django.forms import ModelForm, fields
from .models import Aplicacion


class AplicacionForm(ModelForm):
    class Meta:
        model = Aplicacion
        fields = ['idAplicacion', 'nombreAplicacion', 'archivo_apk','descripcionAplicacion','versionAplicacion']