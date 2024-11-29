from django.shortcuts import render, get_object_or_404
from .models import Post,Autor
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