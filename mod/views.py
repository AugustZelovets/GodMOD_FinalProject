import requests
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from mod.forms import ModInlineFormSet
from .models import Mod, ModVersion
from .forms import *
from .utils import DataMixin


class AllMods(DataMixin, ListView):
    model = Mod
    template_name = 'mod/all_mods.html'
    context_object_name = 'mods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # включает пагинацию, объекты списка(queryset), посты(что идентично), объект представления
        c_def = self.get_user_context(title="Главная страница")  # title, menu(header), categories in sidebar, cat_selected
        return {**context, **c_def}

class GetModDetails(DetailView):
    model = Mod
    template_name = 'mod/get_mod.html'
    context_object_name = 'mod'


class CreateModView(CreateView):
    model = Mod
    template_name = 'mod/create_mod.html'
    form_class = ModCreationForm
    success_url = reverse_lazy('modif:create_mod_version')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateModVersionView(CreateView):
    model = ModVersion
    template_name = 'mod/create_mod_version.html'
    form_class = ModVersionCreationForm
    success_url = reverse_lazy('modif:all_mods')


def create_mod_version(request, slug):
    mod = Mod.objects.filter(slug=slug, author=request.user)
    if request.method == 'POST':
        form = ModVersionCreationForm(request.POST)  # request.FILES)
        if form.is_valid():
            new_mod_version = form.save(commit=False)
            new_mod_version.mod = Mod.objects.get(slug=slug)
            new_mod_version.save()

            return redirect('modif:all_mods')
        return render(request, 'mod/create_mod_version.html', {'form': form, 'title': 'Add new post'})

    form = ModVersionCreationForm()

    return render(request, 'mod/create_mod_version.html', {'form': form, 'title': 'Add new post', 'slug':slug})


def add_mod(request, slug):
    if request.method == 'POST':
        form = ModCreationForm(request.POST)  # request.FILES)

        if form.is_valid():
            new_mod = form.save(commit=False)
            new_mod.save()
            form.save_m2m()

            return redirect(reverse('modif:create_mod_version', kwargs={'slug': new_mod.slug}))

        return render(request, 'mod/create_mod.html', {'form': form, 'title': 'Add new post', 'slug':slug})
    form = ModCreationForm()
    form.category = Category.objects.filter(game__slug = slug)

    return render(request, 'mod/create_mod.html', {'form': form, 'title': 'Add new post', 'slug':slug})


def chose_game(request):
    if request.method == 'POST':
        form = ChoseGameForm(request.POST)  # request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game_slug = form.cleaned_data['game'].slug
            return redirect(reverse('modif:create_mod', kwargs={'slug': game_slug}))
        return render(request, 'mod/chose_game.html', {'form': form, 'title': 'Chose a game'})
    form = ChoseGameForm()
    return render(request, 'mod/chose_game.html', {'form': form, 'title': 'Chose a game'})



class AllGames(ListView):
    model = Game
    template_name = 'mod/all_games.html'
    context_object_name = 'games'


def updated_followings():
    pass


class AllCategoriesView(DataMixin, ListView):
    pass


