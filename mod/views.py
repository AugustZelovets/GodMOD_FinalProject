from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from mod.forms import ModInlineFormSet
from .models import Mod, ModVersion
from .forms import *


class AllMods(ListView):
    model = Mod
    template_name = 'mod/all_mods.html'
    context_object_name = 'mods'


class CreateModView(CreateView):
    template_name = 'mod/create_mod.html'
    model = Mod
    form_class = ModForm

    def get_success_url(self):
        return reverse('all_mods')

    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(CreateModView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = ModForm(self.request.POST)
            ctx['inlines'] = ModInlineFormSet(self.request.POST)
        else:
            print('AAAAAAAAAAAAAAAAAAAAA')
            ctx['form'] = ModForm()
            ctx['inlines'] = ModInlineFormSet()
        return ctx


def all_games():
    pass


def mods_by_category():
    pass


def updated_followings():
    pass


def index():
    pass
