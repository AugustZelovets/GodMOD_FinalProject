from django.urls import path
from .views import *

app_name = 'mod'

urlpatterns = [
    path('', AllMods.as_view(), name='all_mods'),
    path('create_mod/', CreateModView.as_view(), name='create_mod'),
    path('create_mod_version/', CreateModVersionView.as_view(), name='create_mod_version'),

]