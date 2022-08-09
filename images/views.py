from django.views.generic import ListView
from .models import Image
# Create your views here.


class ImageListView(ListView):
    model = Image
    template_name = 'images/show_all.html'
