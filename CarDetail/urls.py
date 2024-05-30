"""
URL configuration for CarDetail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from App.views import List_User,Delete_client,Search_client,Editar_cliente,Logout,Login,StartLogin,Finalizar,Exportar_datos_clientes,Filtrar
from CarDetail import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name="Login"),
    path('logout/',Logout,name="Logout"),
    path('StartLogin/',StartLogin,name="StartLogin"),
    path('list_users/',List_User,name="List_User"),
    path('finish_car/<int:pk>',Finalizar,name="Finalizar"),
    path('eliminar_cliente/<int:pk>',Delete_client,name="Delete_client"),
    path('Editar_cliente/<int:tk>',Editar_cliente,name="Editar_cliente"),
    path('buscar_cliente/',Search_client,name="Search_client"),
    path('filtro/',Filtrar,name="Filtrar"),
    path('exportar_clientes_excel/',Exportar_datos_clientes,name="Exportar_datos_clientes"),
    
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
