from django.contrib import admin

from .models import *

admin.site.register(Game)
admin.site.register(Tag)
admin.site.register(Category)

admin.site.register(Download)

admin.site.register(Mod)
admin.site.register(ModVersion)
