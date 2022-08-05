from django.urls import path
from .views import *

app_name = 'modif'

urlpatterns = [
    path('', AllMods.as_view(), name='all_mods'),
    path('create_mod/<slug>', add_mod, name='create_mod'),
    path('create_mod_version/<slug>', create_mod_version, name='create_mod_version'),
    path('get_mod/<slug>/', GetModDetails.as_view(), name='get_mod'),
    path('categories/<slug:game_slug>', AllGames.as_view(), name='all_games'),
    path('chose_game/', chose_game, name='chose_game')
]


