from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, redirect
from .models import Post,Autor
from .forms import post_Form, post_form_model,AuthorForm
# Create your views here.
def principal(request):
    context = Post.objects.all()
    autores = Autor.objects.all()
    return render(request, 'blog/principal.html', {'posts':context,'autores':autores})

def detalle_post(request, pk):
    context = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post':context})

def segunda(request):
    return render(request, 'blog/segunda.html')

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/autores.html', {'autores':autores})

def detalle_autor(request,pk):
    autor= get_object_or_404(Autor, pk=pk)
    postDeAutores = Post.objects.filter(autor=pk)
    return render(request, 'blog/detalle_autor.html', {'autor':autor,'posts':postDeAutores})

def new(request):
    if request.method == "POST":
        request.POST["titulo"]
    else:
        form = post_Form()
        return render(request, 'blog/new.html')
    

def post_new(request):
    if request.method == "POST":
        form = post_form_model(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            cuerpo = form.cleaned_data["cuerpo"]
            fcreacion = form.cleaned_data["fcreacion"]
            #fcreacion = request.POST["fcreacion"]
            autor = Autor.objects.get(pk=1)
            Post.objects.create(titulo=titulo,autor=autor,cuerpo=cuerpo,fcreacion=fcreacion)
            return render(request, 'blog/post_added.html')
    else:
        form = post_form_model()
    return render(request, 'blog/post_new.html', {"form":form})
    
def post_cambiar(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = post_form_model(request.POST,instance=post)
        if form.is_valid():
            #post.titulo = form.cleaned_data["titulo"]
            #post.cuerpo = form.cleaned_data["cuerpo"]
            #post.fcreacion = form.cleaned_data["fcreacion"]
            #fcreacion = request.POST["fcreacion"]
            #post.save()
            form.save()
            return redirect('principal')
            #return render(request, 'blog/post_added.html')
    else:
        form = post_form_model(instance=post)
    return render(request,"blog/post_cambiar.html",{"form":form})

def form_autor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AuthorForm()
    return render(request,"blog/form_autor.html",{"form":form})

def autor_edit(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = AuthorForm(instance=autor)
    return render(request,"blog/autor_edit.html",{"form":form})

def delete_autor(request,pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect('autores')
    else:
        return render(request,"blog/delete_autor.html",{"autor":autor})