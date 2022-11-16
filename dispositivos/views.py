from django.shortcuts import render
from .models import Dispositivos



def dispositivos(request):
    dispositivos = Dispositivos.objects.all()

    context = {
        'dispositivos': dispositivos,
    }
    
    return render(request, 'dispositivos.html', context)
