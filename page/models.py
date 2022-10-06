from django.db import models

from mod.models import Mod


class Comment(models.Model):
    #mod_version = models.ForeignKey(ModVersion, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f'by {self.author} at {self.created} in v.{self.mod_version}'

    class Meta:
        pass


class Page(models.Model):  # mod / game / article??
    #title = models.CharField(max_length=255, unique=True, db_index=True)
    #mod = models.ForeignKey(Mod, on_delete=models.SET_NULL, blank=True, null=True)
    # author = models.CharField(max_length=50)
    #created = models.DateField(auto_now=True)
    #text = models.TextField()
    #published = models.BooleanField()
    # image = models.ImageField(blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, editable=False, blank=True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        pass


class Modpack(models.Model):
    name = models.CharField(max_length=50)
    mods = models.ManyToManyField(Mod)
    author = models.CharField(max_length=50)
    is_public = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        pass
