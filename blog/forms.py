from django import forms
from django.forms import ModelForm, Textarea
from .models import Post, Autor
from datetime import date
from django.core.exceptions import ValidationError
class post_Form(forms.Form):
    titulo = forms.CharField(label="Título",max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fcreacion = forms.DateField(label="Fecha de publicacion")
    contacto = forms.EmailField(label="Correo Electronico")
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label="Autor")

class post_form_model(forms.ModelForm):
    fcreacion = forms.DateField(label='Fecha de creacion')
    class Meta:
        model = Post
        fields = '__all__'
    
    def clean_fcreacion(self):
        fcreacion = self.cleaned_data['fcreacion']
        if fcreacion > date.today():
            raise ValidationError("La fecha introducida no puede ser mas grande que la de hoy.")
        return fcreacion

class AuthorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__' 
    
    def clean_fnacimiento(self):
        fnacimiento = self.cleaned_data['fnacimiento']
        if fnacimiento > date.today():
            raise ValidationError("No se admiten viajeros del tiempo")
        return fnacimiento
