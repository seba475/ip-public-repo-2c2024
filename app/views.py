# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def index_page(request):
    return render(request, 'index.html')

def home(request):
    # Llama al servicio para obtener las imágenes desde la API
    images = services.getAllImages()

    # Obtiene los favoritos del usuario si está autenticado; de lo contrario, asigna una lista vacía.
    if request.user.is_authenticated:
        favourite_list = services.getAllFavourites(request)
    else:
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

    # Obtiene la lista de favoritos del usuario autenticado (si corresponde)
    favourite_list = services.getAllFavourites(request) if request.user.is_authenticated else []

    # Renderiza el template con las imágenes filtradas o todas
    return render(request, 'home.html', {'images': images,'favourite_list': favourite_list})

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    # Obtiene todos los favoritos del usuario logueado desde la capa de servicios
    favourite_list = services.getAllFavourites(request)
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    if request.method == 'POST':
        # Llamamos a la capa de servicios para guardar el favorito
        services.saveFavourite(request)
    return redirect('home')  # Redirigimos de vuelta a la galería

@login_required
def deleteFavourite(request):
    if request.method == 'POST':
        # Llamamos a la capa de servicios para eliminar el favorito
        services.deleteFavourite(request)
    return redirect('favoritos')  # Redirigimos de vuelta a la sección de favoritos

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