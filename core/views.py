from django.shortcuts import redirect, render
from .models import Aplicacion
from .forms import AplicacionForm
from django.http import HttpResponse


# Create your views here.


def home(request):
    data = { 'list' : Aplicacion.objects.all().order_by('nombreAplicacion') }
    return render(request, "core/home.html", data)

def apks(request, id):
    data = { 'aplicacion': Aplicacion.objects.get(idAplicacion=id)}
    return render(request, 'core/apks.html', data)

def test(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    print(user_agent)
    if 'Mozilla' in user_agent:
        mensaje = 'Estás usando un navegador compatible con Mozilla.'
    else:
        mensaje = 'No estás usando un navegador compatible con Mozilla.'

    return render(request, 'core/test.html', {'mensaje': user_agent})