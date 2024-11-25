# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

@login_required
def exit(request):
    pass