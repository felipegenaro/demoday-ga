"""demoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from landing_principal.views import render_index
from contato_page.views import adicionar_contato
from indice_poluentes.views import retorna_poluentes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index, name='home'),
    path('contato/', adicionar_contato, name='contato'),
    path('indice_poluentes/', retorna_poluentes, name='poluentes'),
]
