from django import forms
from django.forms import ModelForm, Textarea
from .models import Post, Autor
class post_Form(forms.Form):
    titulo = forms.CharField(label="Título",max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fcreacion = forms.DateField(label="Fecha de publicacion")
    contacto = forms.EmailField(label="Correo Electronico")
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label="Autor")

class post_form_model(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class AuthorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'