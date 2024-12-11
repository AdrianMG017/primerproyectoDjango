from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal, name='principal' ),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('new', views.post_new, name='post_new'),
    path('post/cambiar/<int:pk>', views.post_cambiar, name='post_cambiar'),
    path('autores', views.autores, name='autores'),
    path('autor/<int:pk>', views.detalle_autor, name='detalle_autor'),
    path('autor/new', views.form_autor, name='form_autor'),
    path('autor/<int:pk>/edit', views.autor_edit, name='autor_edit'),
    path('autor/<int:pk>/delete', views.delete_autor, name='delete_autor'),
    path('segunda', views.segunda, name='segunda')
]