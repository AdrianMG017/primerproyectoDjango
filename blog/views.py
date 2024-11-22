from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def segunda(request):
    return render(request, 'segunda.html')