from django.urls import path
from my_app import views


app_name = "my_app" 
urlpatterns = [
    path('destinos', view = views.destinos, name="destino-list"),
    path('destino/add', view = views.create_destinos, name="destino-add"),
]