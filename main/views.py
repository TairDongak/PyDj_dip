from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'tasks': tasks })

#Шапкич + ссылка на тест_______________________________________

def content(request):
    return render(request, "main/content.html")


def about(request):
    return render(request, "main/about.html")


def test(request):
    return render(request, "main/testing.html")


#Глава 1_______________________________________________________

def install(request):
    return render(request, "main/1/install.html")


def vvod(request):
    return render(request, "main/1/vvod.html")


def projects(request):
    return render(request, "main/1/projects.html")

def first(request):
    return render(request, "main/1/first.html")


def prilo(request):
    return render(request, "main/1/prilo.html")

#Глава 2_______________________________________________________

def zapros(request):
    return render(request, "main/2/zapros.html")



def path(request):
    return render(request, "main/2/path.html")

def imagine(request):
    return render(request, "main/2/imagine.html")


def parametrs(request):
    return render(request, "main/2/parametrs.html")    

def talker(request):
    return render(request, "main/2/Code_talker.html")   

#Глава 3_________________________________________________________

def template(request):
    return render(request, "main/3/template.html")

def data_template(request):
    return render(request, "main/3/data_template.html")
    
def static_files(request):
    return render(request, "main/3/static_files.html")  

def template_view(request):
    return render(request, "main/3/template_view.html")  

def config(request):
    return render(request, "main/3/config.html")

def rasshir(request):
    return render(request, "main/3/rasshir.html")

#Глава 4_________________________________________________________

def forms(request):
    return render(request, "main/4/forms.html")

def types(request):
    return render(request, "main/4/types.html")

def poles(request):
    return render(request, "main/4/poles.html")

def valid(request):
    return render(request, "main/4/valid.html")

def dsettings(request):
    return render(request, "main/4/dsettings.html")

def stylepole(request):
    return render(request, "main/4/stylepole.html")

#Глава 5_________________________________________________________

def modmigr(request):
    return render(request, "main/5/modmigr.html")

def typepole(request):
    return render(request, "main/5/typepole.html")

def crud(request):
    return render(request, "main/5/crud.html")

def objmodel(request):
    return render(request, "main/5/objmodel.html")

def reddel(request):
    return render(request, "main/5/reddel.html")    

def onetomany(request):
    return render(request, "main/5/onetomany.html") 

def manytomany(request):
    return render(request, "main/5/manytomany.html")     

def onetoone(request):
    return render(request, "main/5/onetoone.html")     

    