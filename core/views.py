from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'core/home.html')
def Pagina2(request):
    return render (request,'core/pagina2.html')