# capa de servicio/lógica de negocio

from ..transport.transport import getAllImages as fetch_images  # Función para obtener datos de la API
from ..utilities.translator import fromRequestIntoCard # Función para transformar datos crudos en una Card
from django.contrib.auth import get_user

def getAllImages(input=None):

    #Obtiene un listado de datos desde la API de Rick & Morty. 
    # Si se pasa un filtro (input), trae solo los datos relacionados con ese filtro.

    # Obtiene datos crudos desde la API
    if input:
        json_collection = fetch_images(input)  # Con filtro
    else:
        json_collection = fetch_images()  # Sin filtro

    # Transformar los datos crudos en objetos Card
    images = []
    for item in json_collection:
        card = fromRequestIntoCard(item)  # Convierte cada elemento en un formato manejable
        images.append(card)

    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.