from django.shortcuts import render
from django.views.generic import ListView , DetailView , DeleteView, CreateView , UpdateView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snacks_list'


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['title','description','purchaser']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'description']


    
class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url=reverse_lazy("snack_list")