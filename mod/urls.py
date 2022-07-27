from django.urls import path
from .views import *

urlpatterns = [
    path('', AllMods.as_view(), name='all_mods'),
    path('create_mod/', CreateModView.as_view(), name='create_mod')
]