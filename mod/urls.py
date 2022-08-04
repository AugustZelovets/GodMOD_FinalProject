from django.urls import path
from .views import *

app_name = 'mod'

urlpatterns = [
    path('', AllMods.as_view(), name='all_mods'),
    path('create_mod/', add_mod, name='create_mod'),
    path('create_mod_version/', create_mod_version, name='create_mod_version'),
    path('get_mod/<slug>/', GetModDetails.as_view(), name='get_mod'),

]


