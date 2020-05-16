from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.WidgetCreate.as_view(), name='widget_create'),

]
