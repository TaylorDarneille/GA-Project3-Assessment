from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Widget



# Define the home view
def home(request):
  # there was no code yet to retrieve the widgets from the db and send them to the home.html template
  widgets = Widget.objects.all()
  return render(request, 'home.html', { 'widgets':widgets })
  # return render(request, 'home.html')


class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = '/'  


class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'  