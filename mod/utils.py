from mod.models import *


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):

        context = kwargs
        games = Game.objects.all()

        context['games'] = games
        return context