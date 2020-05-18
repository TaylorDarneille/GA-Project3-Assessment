from django.forms import ModelForm
from .models import Widget

# You are correct that this is needed to render the add widget form on the home page, but you didn't actually define the ModelForm
# class WidgetForm(ModelForm):
#     class Meta:
#         model = Widget