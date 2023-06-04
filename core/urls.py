from django.urls import path
from .views import home 
from .views import Pagina2, mod_vehiculo, listar_mod_vehiculo
urlpatterns=[
    path('', home, name="home"),
    path('pagina2', Pagina2, name="pagina2"),
    path('mod_vehiculo <id>', mod_vehiculo, name="mod_vehiculo"),
    path('listar_mod_vehiculo', listar_mod_vehiculo, name="listar_mod_vehiculo"),
]