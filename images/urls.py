from django.urls import path, include
from django.views.generic import TemplateView
from .views import ImageListView

app_name = 'images'

urlpatterns = [
    path('', TemplateView.as_view(template_name='base/index.html')),
    path('images/', ImageListView.as_view(), name='images'),
]
