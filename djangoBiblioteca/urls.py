"""
URL configuration for djangoBiblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from libros import views as libros_views
from clientes import views as clientes_views
from django.contrib.auth import views as auth_views
# from django.contrib.auth import login

#Para crud libros
from libros.views import (LibroListView,LibroCreate, LibroDelete, LibroUpdate)
#Para crud clientes
from clientes.views import (ClientesListView,ClientesCreate, ClientesDelete, ClientesUpdate)

urlpatterns = [
    path('',views.home, name='home'),
    path('acercade/',views.acercade, name='acercade'),
    path('contacto/',views.contacto, name='contacto'),
    path('buscar/',libros_views.buscarlib, name='buscarQ'),
    path('modificarLibros/',libros_views.modifBusc, name='buscarM'),
    path('buscarPrestamo/',clientes_views.buscarPrest, name='buscarL'),
    path('admin/', admin.site.urls),

    #Para el listado de Libros   
    path('libro_list/', LibroListView.as_view(), name="listarLibros"),
    #Para crear
    path('libro_form/', LibroCreate.as_view(), name='create'),
    #Para modificar
    path('libro_update_form/<int:pk>/', LibroUpdate.as_view(), name='update'),
    #Para eliminar
    path('libro_confirm_delete/<int:pk>/', LibroDelete.as_view(), name='delete'),
    path('admin/', admin.site.urls),

    #Para el listado de Clientes   
    path('buscarPrestamo/', ClientesListView.as_view(), name="buscarL"),
    #Para crear
    path('clientes_form/', ClientesCreate.as_view(), name='createCliente'),
    #Para modificar
    path('clientes_update_form/<int:pk>/', ClientesUpdate.as_view(), name='updateCliente'),
    #Para eliminar
    path('clientes_confirm_delete/<int:pk>/', ClientesDelete.as_view(), name='deleteCliente'),
    path('admin/', admin.site.urls),
    #Para login
    # path('',login,{'template_name':'login.html'},name='login')
    path("login/", auth_views.LoginView.as_view()),
    
]
#configuracion extendida para mostrar las imagenes en modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
 