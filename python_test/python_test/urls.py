"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from python_test import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    path(
        "client/",
        views.ClientListView.as_view(),
        name="client_list"
    ),
    path(
        "client/create/",
        views.ClientCreateView.as_view(),
        name="client_create"
    ),
    path(
        "client/<int:pk>",
        views.ClientUpdateView.as_view(),
        name="client_update"
    ),
    path(
        "client/<int:pk>/delete/",
        views.ClientDeleteView.as_view(),
        name="client_delete"
    ),
]
