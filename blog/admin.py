from django.contrib import admin

# Register your models here.
from .models import Post,Autor

admin.site.register(Post)
admin.site.register(Autor)