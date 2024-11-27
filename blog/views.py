from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def principal(request):
    context = Post.objects.all()
    autores = Post.objects.values_list('autor',flat=True).distinct()
    return render(request, 'blog/principal.html', {'posts':context,'autores':autores})

def detalle_post(request, pk):
    context = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post':context})

def segunda(request):
    return render(request, 'blog/segunda.html')