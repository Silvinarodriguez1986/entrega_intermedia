from django.urls import path
from my_app import views 


app_name = "my_app" 
urlpatterns = [
    path("destinos", view=views.destinos, name="destino-list"),
    path("destino/add", view=views.create_destinos, name="destino-add"),
    path("visas", view=views.visas, name="visa-list"),
    path("visa/add", view=views.create_visas, name="visa-add"),
    path("requisitos", view=views.requisitos, name="requisito-list"),
    path("requisito/add", view=views.create_requisitos, name="requisito-add"),
    

]












