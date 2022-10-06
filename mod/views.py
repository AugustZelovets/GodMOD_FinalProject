from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import *
from .utils import DataMixin


class AllGames(ListView):
    model = Game
    template_name = 'mod/all_games.html'
    context_object_name = 'games'


def chose_game(request):
    if request.method == 'POST':
        form = ChoseGameForm(request.POST)
        if form.is_valid():
            game_slug = form.cleaned_data['game'].slug
            return redirect(reverse('modif:add_mod', kwargs={'slug': game_slug}))
        return render(request, 'mod/chose_game.html', {'form': form, 'title': 'Chose a game'})
    form = ChoseGameForm()
    return render(request, 'mod/chose_game.html', {'form': form, 'title': 'Chose a game'})


class AllMods(DataMixin, ListView):
    model = Mod
    template_name = 'mod/all_mods.html'
    context_object_name = 'mods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return {**context, **c_def}


class ModCategoriesForGame(DataMixin, ListView):
    model = Category
    template_name = 'mod/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(game__slug=self.kwargs['game_slug'])


class ModsByCategory(DataMixin, ListView):
    model = Mod
    context_object_name = 'mods'
    template_name = 'mod/mods_by_category.html'

    def get_queryset(self):
        return Mod.objects.filter(category__slug=self.kwargs['category_slug'])


class ModDetails(DetailView):
    model = Mod
    template_name = 'mod/get_mod.html'
    context_object_name = 'mod'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mod_versions'] = ModVersion.objects.filter(mod__slug=self.kwargs['slug'])
        return context


def add_modversion(request, slug):
    if request.method == 'POST':
        form = ModVersionCreationForm(request.POST, request.FILES)
        if form.is_valid():
            new_mod_version = form.save(commit=False)
            new_mod_version.mod = Mod.objects.get(slug=slug)
            new_mod_version.save()
            form.save()
            return redirect('modif:all_mods')
        return render(request, 'mod/add_modversion.html', {'form': form, 'title': 'Add new post'})
    form = ModVersionCreationForm()
    return render(request, 'mod/add_modversion.html', {'form': form, 'title': 'Add new post', 'slug': slug})


def add_mod(request, slug):
    if request.method == 'POST':
        form = ModCreationForm(request.POST, request.FILES)

        if form.is_valid():
            new_mod = form.save(commit=False)
            new_mod.save()
            form.save_m2m()
            return redirect(reverse('modif:add_modversion', kwargs={'slug': new_mod.slug}))

        return render(request, 'mod/add_mod.html', {'form': form, 'title': 'Add new post', 'slug': slug})
    form = ModCreationForm()
    form.fields['category'].queryset = Category.objects.filter(game__slug=slug)

    return render(request, 'mod/add_mod.html', {'form': form, 'title': 'Add new post', 'slug': slug})






# class CreateModView(CreateView):
#     model = Mod
#     template_name = 'mod/add_mod.html'
#     form_class = ModCreationForm
#     success_url = reverse_lazy('modif:add_modversion')
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         print(' CLASS WORKS')
#         return super().form_valid(form)
#
#
# class CreateModVersionView(CreateView):
#     model = ModVersion
#     template_name = 'mod/add_modversion.html'
#     form_class = ModVersionCreationForm
#     success_url = reverse_lazy('modif:all_mods')
