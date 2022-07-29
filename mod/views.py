from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from mod.forms import ModInlineFormSet
from .models import Mod, ModVersion
from .forms import *


class AllMods(ListView):
    model = Mod
    template_name = 'mod/all_mods.html'
    context_object_name = 'mods'


class CreateModView(CreateView):
    model = Mod
    template_name = 'mod/create_mod.html'
    form_class = ModCreationForm
    success_url = reverse_lazy('mod:create_mod_version')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateModVersionView(CreateView):
    model = ModVersion
    template_name = 'mod/create_mod_version.html'
    form_class = ModVersionCreationForm
    success_url = reverse_lazy('mod:all_mods')





# class CreateModView(CreateView):
#     template_name = 'mod/create_mod.html'
#     model = Mod
#     form_class = ModForm
#
#     def get_success_url(self):
#         return reverse('all_mods')
#
#     def form_valid(self, form):
#         ctx = self.get_context_data()
#         print(ctx)
#         inlines = ctx['inlines']
#         if inlines.is_valid() and form.is_valid():
#             print(form.cleaned_data)
#             print('MODMOD', inlines.cleaned_data[0]['mod'], )
#
#             self.object = form.save(commit=False)
#             inlines.cleaned_data[0]['mod'] = form.cleaned_data['name']
#             inlines.cleaned_data[0]['id'] = 3
#
#             #inlines.save()
#             self.object.save()
#             print('self.object',
#                 self.object
#             )
#             print('MODMOD', inlines.cleaned_data, )
#
#             return redirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))
#
#     def get_context_data(self, **kwargs):
#         ctx = super(CreateModView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             ctx['form'] = ModForm(self.request.POST, self.request.FILES,)
#             ctx['inlines'] = ModInlineFormSet(self.request.POST, self.request.FILES,)
#         else:
#             ctx['form'] = ModForm()
#             ctx['inlines'] = ModInlineFormSet()
#         return ctx


# def manage_articles(request):
#     ModFormSet = formset_factory(ModForm)
#     ModVersionFormSet = formset_factory(ModVersionForm)
#
#     if request.method == 'POST':
#         mod_formset = ModFormSet(request.POST, request.FILES, prefix='mod')
#         modversion_formset = ModVersionFormSet(request.POST, request.FILES, prefix='modversion')
#         if mod_formset.is_valid() and modversion_formset.is_valid():
#             new_mod = mod_formset.save()
#             new_modversion_formset = modversion_formset.save()
#
#     else:
#         mod_formset = ModFormSet(prefix='mod')
#         modversion_formset = ModVersionFormSet(prefix='modversion')
#     return render(request, 'mod/manage_articles.html', {
#         'mod_formset': mod_formset,
#         'modversion_formset': modversion_formset,
#     })


class AllGames(ListView):
    model = Game
    template_name = 'mod/all_games.html'
    context_object_name = 'games'

# class AllModsForGame
#
# class ModsByCategory
#
#



def updated_followings():
    pass


