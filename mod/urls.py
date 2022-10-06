from django.urls import path
from .views import *

app_name = 'modif'

urlpatterns = [
    path('', AllMods.as_view(), name='all_mods'),
    path('add_mod/<slug>', add_mod, name='add_mod'),
    path('add_modversion/<slug>', add_modversion, name='add_modversion'),
    path('mod/<slug>/', ModDetails.as_view(), name='get_mod'),
    path('chose_game/', chose_game, name='chose_game'),
    path('<game_slug>/categories/', ModCategoriesForGame.as_view(), name='categories'),
    path('<category_slug>/', ModsByCategory.as_view(), name='mods_by_category'),

]
