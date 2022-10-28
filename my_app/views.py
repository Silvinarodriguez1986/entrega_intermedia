

from django.contrib import messages
from django.shortcuts import render

from my_app.models import Destino
from my_app.forms import DestinoForm


def create_destinos(request):
    if request.method == "POST":
        destino_form = DestinoForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if destino_form.is_valid():
            data = destino_form.cleaned_data
            actual_objects = Destino.objects.filter(
                pais=data["pais"], poblacion=data["poblacion"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El destino {data['pais']} - {data['poblacion']} ya está creado",
                )
            else:
                destino = Destino(pais=data["pais"], poblacion=data["poblacion"])
                destino.save()
                messages.success(
                    request,
                    f"Destino {data['pais']} - {data['poblacion']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"destinos": Destino.objects.all()},
                template_name="my_app/destino_list.html",
            )

    destino_form = DestinoForm(request.POST)
    context_dict = {"form": destino_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/destino_form.html",
    )

def destinos(request):
    return render(
        request=request,
        context={"destinos": Destino.objects.all()},
        template_name="my_app/destino_list.html",
    )

