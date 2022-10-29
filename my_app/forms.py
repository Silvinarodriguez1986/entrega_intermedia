from django import forms



class DestinoForm(forms.Form):
    pais = forms.CharField(
        label="Pais:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "destino-pais",
                "placeholder": "ingrese el pais",
                "required": "True",
            }
        ),
    )
    poblacion = forms.IntegerField(
        label="Poblacion:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "destino-poblacion",
                "placeholder": "ingrese la cantidad",
                "required": "True",
            }
        ),
    )


    
class VisaForm(forms.Form):
    tipo = forms.CharField(
        label="Tipo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "visa-tipo",
                "placeholder": "ingrese el tipo de visa",
                "required": "True",
            }
        ),
    )
    costo = forms.IntegerField(
        label="Costo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "visa-costo",
                "placeholder": "ingrese el valor",
                "required": "True",
            }
        ),
    )


class RequisitoForm(forms.Form):
    visa = forms.CharField(
        label="Visa:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "requisito-visa",
                "placeholder": "ingrese visa requerida",
                "required": "True",
            }
        ),
    )

    estudio = forms.CharField(
        label="Estudio:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "requisito-estudio",
                "placeholder": "ingrese estudio requerido",
                "required": "True",
            }
        ),
    )
    edad = forms.IntegerField(
        label="Edad:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "requisito-edad",
                "placeholder": "ingrese la edad",
                "required": "True",
            }
        ),
    )





    



