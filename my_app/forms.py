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


