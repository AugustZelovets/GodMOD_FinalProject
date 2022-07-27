from django.shortcuts import render

from page.models import Page






def get_page(request):
    page = Page.objects.get(pk=1)
    mod = page.mod
    modversion = mod.modversion_set.all()

    context = {
        'page': page,
        'mod': mod,
        'modversion': modversion,

    }
    return render(request, 'page/index.html', context)