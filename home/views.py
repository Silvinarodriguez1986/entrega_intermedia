from django.shortcuts import render

from django.db.models import Q
from my_app.models import Visa
from my_app.forms import VisaForm





def index(request):
    return render( 
        request=request,
        context={},
        template_name="home/index.html",
    )


 
def search(request):
    busqueda = request.GET.get("buscar")
    visas = Visa.objects.all()
    
    if busqueda:
        visas = Visa.objects.filter(
            Q(tipo__icontains = busqueda) |
            Q(costo__icontains = busqueda)

        ).distinct()
        
    return render(request, 'index.html', {'visas':visas})