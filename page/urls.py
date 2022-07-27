from django.urls import path

from .views import *

urlpatterns = [
    path('', get_page, name='get_page')

]