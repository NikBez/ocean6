from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    re_path(r'collection-[0-9]{2}/', catalog, name="catalog"),
]