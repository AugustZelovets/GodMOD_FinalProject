from django.urls import path

from .views import *

app_name = 'page'

urlpatterns = [
    path('', get_page, name='get_page')

]