from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
