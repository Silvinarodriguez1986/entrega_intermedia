

from django.contrib import messages
from django.shortcuts import render

from my_app.models import Destino
from my_app.forms import DestinoForm

from my_app.models import Visa
from my_app.forms import VisaForm

from my_app.models import Requisito
from my_app.forms import RequisitoForm 




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




def create_visas(request):
    if request.method == "POST":
        visa_form = VisaForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if visa_form.is_valid():
            data = visa_form.cleaned_data
            actual_objects = Visa.objects.filter(
                tipo=data["tipo"], costo=data["costo"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La visa {data['tipo']} - {data['costo']} ya está creado",
                )
            else:
                visa = Visa(tipo=data["tipo"], costo=data["costo"])
                visa.save()
                messages.success(
                    request,
                    f"Visa {data['tipo']} - {data['costo']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"visas": Visa.objects.all()},
                template_name="my_app/visa_list.html",
            )

    visa_form = VisaForm(request.POST)
    context_dict = {"form": visa_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/visa_form.html",
    )

def visas(request):
    return render(
        request=request,
        context={"visas": Visa.objects.all()},
        template_name="my_app/visa_list.html",
    )


def create_requisitos(request):
    if request.method == "POST":
        requisito_form = RequisitoForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if requisito_form.is_valid():
            data = requisito_form.cleaned_data
            actual_objects = Requisito.objects.filter(
                visa=data["visa"], estudio=data["estudio"], edad=data["edad"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Los requisitos {data['visa']} - {data['estudio']} - {data['edad']} ya está creado",
                )
            else:
                requisito = Requisito(visa=data["visa"], estudio=data["estudio"], edad=data["edad"])
                requisito.save()
                messages.success(
                    request,
                    f"Requisito {data['visa']} - {data['estudio']} - {data['edad']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"requisitos": Requisito.objects.all()},
                template_name="my_app/requisito_list.html",
            )

    requisito_form = RequisitoForm(request.POST)
    context_dict = {"form": requisito_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/requisito_form.html",
    )

def requisitos(request):
    return render(
        request=request,
        context={"requisitos": Requisito.objects.all()},
        template_name="my_app/requisito_list.html",
    )




