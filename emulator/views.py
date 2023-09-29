from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from allauth.account.views import LoginView, SignupView
from .models import *
from .forms import ProyectoForm
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'contenido.html')

@login_required
def profile(request):
    # Obtener la información del usuario autenticado
    user = request.user
    # Puedes agregar más detalles según tus necesidades, como el nombre, la dirección, etc.

    return render(request, 'profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('emulator:index')

class CustomLoginView(LoginView):
    template_name = 'socialaccount/login.html'

class CustomSignupView(SignupView):
    template_name = 'socialaccount/signup.html'
    
def mis_proyectos(request):
    if request.user.is_authenticated:
        proyectos = Proyecto.objects.filter(usuario=request.user)
        return render(request, 'mis_proyectos.html', {'proyectos': proyectos})
    else:
        return render(request, 'socialaccount/login.html')  # Otra página para cuando el usuario no está autenticado
    
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            return redirect('emulator:mis_proyectos')  # Redirige a la lista de proyectos
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})

def cargar_archivo(request):
    if request.method == 'POST' and request.FILES.get('archivo_xml'):
        archivo = request.FILES['archivo_xml']
        # Aquí puedes procesar el archivo, por ejemplo, guardarlo en el sistema
        # y realizar cualquier procesamiento necesario
        return redirect('ruta_de_exito')  # Redirige a la página de éxito
    return render(request, 'cargar_archivo.html')

def generar_contenido_xml():
    # Aquí generas el contenido XML utilizando librerías o formateando manualmente el XML
    contenido = '<?xml version="1.0" encoding="UTF-8"?>\n'
    contenido += '<root>\n'
    contenido += '    <elemento>Contenido del elemento</elemento>\n'
    # ... Agrega más contenido XML según tus necesidades ...
    contenido += '</root>\n'
    return contenido

def exportar_xml(request):
    contenido_xml = generar_contenido_xml()

    response = HttpResponse(contenido_xml, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="archivo.xml"'
    return response

def ejemplos(request):
    ejemplos = Ejemplo.objects.all()
    return render(request, 'ejemplos.html', {'ejemplos': ejemplos})

def detalle_ejemplo(request, ejemplo_id):
    ejemplo = get_object_or_404(Ejemplo, pk=ejemplo_id)
    return render(request, 'detalle_ejemplo.html', {'ejemplo': ejemplo})

@login_required
def profile(request):
    user = request.user

    return render(request, 'profile.html', {'user': user})