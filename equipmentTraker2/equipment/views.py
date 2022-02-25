from django.views.generic import TemplateView,ListView, DetailView, View, CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .forms import equipmentForm
from django.http import HttpResponse
# from django.contrib.auth.decorators import  login_required
from django.urls import  reverse_lazy
from . import models
from django.http import HttpResponse
# from .forms import FarForm
# from .filters import FARfilter
# from django import forms
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# Create your views here.

# Create your views here.
def index(requst):
    return HttpResponse("He there")


class equipmentListView(ListView):
# class equipmentListView(View):
    template_name = 'equipment/equipment-home.html'
    context_object_name = 'equipmentall'
    queryset = models.equipment.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = FARfilter(self.request.GET, queryset=self.queryset)
    #     return context


class equipmentCreateView(CreateView):
    template_name = 'equipment/equipment-new.html'
    form_class = equipmentForm
    model = models.equipment
    success_url = reverse_lazy('equipment')

    def from_valid(self,form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)
