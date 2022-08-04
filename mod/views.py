import requests
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from mod.forms import ModInlineFormSet
from .models import Mod, ModVersion
from .forms import *


class AllMods(ListView):
    model = Mod
    template_name = 'mod/all_mods.html'
    context_object_name = 'mods'


class GetModDetails(DetailView):
    model = Mod
    template_name = 'mod/get_mod.html'
    context_object_name = 'mod'


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


def create_mod_version(request, mod_slug):
    mod = Mod.objects.get(slug=mod_slug, author=request.user)
    if request.method == 'POST':
        form = ModVersionCreationForm(request.POST)  # request.FILES)
        if form.is_valid():
            new_mod_version = form.save(commit=False)
            new_mod_version.mod = Mod.objects.get(slug=mod_slug)
            new_mod_version.save()

            return redirect('mod:all_mods')
        return render(request, 'mod/create_mod_version.html', {'form': form, 'title': 'Add new post'})

    form = ModVersionCreationForm()

    return render(request, 'mod/create_mod_version.html', {'form': form, 'title': 'Add new post', 'slug':mod_slug})


def add_mod(request):
    if request.method == 'POST':
        form = ModCreationForm(request.POST)  # request.FILES)
        if form.is_valid():
            new_mod = form.save(commit=False)
            new_mod.save()
            form.save_m2m()


            return redirect(reverse('mod:create_mod_version', kwargs={'slug': new_mod.slug}))

        return render(request, 'mod/create_mod.html', {'form': form, 'title': 'Add new post'})
    form = ModCreationForm()
    return render(request, 'mod/create_mod.html', {'form': form, 'title': 'Add new post'})



class AllGames(ListView):
    model = Game
    template_name = 'mod/all_games.html'
    context_object_name = 'games'




def updated_followings():
    pass




