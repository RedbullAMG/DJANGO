from django.urls import path
from .views import home 
from .views import Pagina2
urlpatterns=[
    path('', home, name="home"),
    path('pagina2', Pagina2, name="pagina2"),
]