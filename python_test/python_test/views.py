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
        filter_by = self.request.GET.get('filter-by')
        if query:
            if filter_by == 'name':
                filtered_result = models.Client.objects.filter(name__contains=query)
            elif filter_by == 'email':
                filtered_result = models.Client.objects.filter(email_address__contains=query)
            elif filter_by == 'phone':
                filtered_result = models.Client.objects.filter(phone_number__contains=query)
            else:
                filtered_result = models.Client.objects.filter(suburb__contains=query)
            return filtered_result
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
    success_url = reverse_lazy("client_list")


class ClientDeleteView(DeleteView):
    model = models.Client

    success_url = reverse_lazy("client_list")
