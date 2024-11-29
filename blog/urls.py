from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal, name='principal' ),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('autores', views.autores, name='autores'),
    path('autor/<int:pk>', views.detalle_autor, name='detalle_autor'),
    path('segunda', views.segunda, name='segunda')
]