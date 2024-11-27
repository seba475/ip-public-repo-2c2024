# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    # Llama al servicio para obtener las imágenes desde la API
    images = services.getAllImages()

    # Lista vacía de favoritos (no desarrollada esta funcionalidad)
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

def search(request):
    # Obtiene el mensaje de búsqueda ingresado por el usuario
    search_msg = request.POST.get('query', '').strip()

    if search_msg:
        # Si se ingresó un texto, filtra las imágenes según el criterio
        images = services.getAllImages(input=search_msg)
    else:
        # Si no se ingresó texto, muestra todas las imágenes (igual que en 'home')
        images = services.getAllImages()

    # Lista vacía de favoritos (no desarrollada esta funcionalidad)
    favourite_list = []

    # Renderiza el template con las imágenes filtradas o todas
    return render(request, 'home.html', {'images': images,'favourite_list': favourite_list})

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

def login_view(request):
    if request.method == 'POST':  # Verifica que la solicitud sea POST (envío del formulario)
        username = request.POST.get('username')  # Extrae el nombre de usuario del formulario
        password = request.POST.get('password')  # Extrae la contraseña del formulario
    
        # Valida si las credenciales ingresadas coinciden con las predefinidas
        if username == 'admin' and password == 'admin':
            user = User.objects.get(username='admin')  # Busca al usuario "admin" en la base de datos
            login(request, user)  # Inicia sesión para el usuario encontrado
            return redirect('home')  # Redirige al usuario a la página principal

# Vista para cerrar sesión
@login_required
def exit(request):
    logout(request) # Cerramos la sesión del usuario
    return redirect('index-page')  # Redirige al inicio