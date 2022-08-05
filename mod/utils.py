from mod.models import *


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):

        context = kwargs
        games = Game.objects.all()

        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        #context['menu'] = user_menu
        context['games'] = games
        return context