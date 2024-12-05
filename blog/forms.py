from django import forms

class post_Form(forms.Form):
    titulo = forms.CharField(label="Título",max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fcreacion = forms.DateField(label="Fecha de publicacion")