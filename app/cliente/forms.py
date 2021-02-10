from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = ['CiRuc','nombres','apellidos','direccion','esRucPasaporte','estado']
        labels = {'CiRuc':"Ci-Ruc o pasaporte",
               "estado":"Estado"}
        widget={
            'CiRuc': forms.TextInput,
            'nombres': forms.TextInput,
            'apellidos': forms.TextInput,
            'direccion': forms.TextInput,
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
