from django.db.models import Manager
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from python_test import models


# Insert views here
class ClientListView(ListView):
    model = models.Client

    fields = [
        "name",
        "street_address",
        "suburb",
        "postcode",
        "state",
        "contact_name",
        "email_address",
        "phone_number"
    ]

    success_url = reverse_lazy("client_list")

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return models.Client.objects.filter(name__contains=query)
        else:
            return models.Client.objects.all()


class ClientCreateView(CreateView):
    model = models.Client

    fields = [
        "name",
        "street_address",
        "suburb",
        "postcode",
        "state",
        "contact_name",
        "email_address",
        "phone_number"
    ]
    success_url = reverse_lazy("client_list")


class ClientUpdateView(UpdateView):
    model = models.Client

    fields = [
        "name",
        "street_address",
        "suburb",
        "postcode",
        "state",
        "contact_name",
        "email_address",
        "phone_number"
    ]


class ClientDeleteView(DeleteView):
    model = models.Client

    success_url = reverse_lazy("client_list")
