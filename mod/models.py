from django.db import models
from django.urls import reverse



class Game(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='GameImages/%Y/%m/%d')
    date = models.DateField()
    genre = models.CharField(max_length=30)
    team = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('modif:categories', kwargs={'game_slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        pass


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('modif:mods_by_category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'


class Mod(models.Model):
    name = models.CharField(max_length=30, unique=True, )
    slug = models.SlugField(max_length=30, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='ModMainImages/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    author = models.CharField(max_length=30)
    tag = models.ManyToManyField(Tag, blank=True)
    likes = models.IntegerField(default=0, editable=False)
    description = models.CharField(max_length=255)

    #published = models.BooleanField()
    #text = models.TextField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('modif:get_mod', kwargs={'slug': self.slug})

    class Meta:
        pass


class ModVersion(models.Model):
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=30, unique=True)
    version = models.CharField(max_length=10, default='1.0', )
    files = models.FileField(null=True, blank=True, upload_to='ModFiles/%Y/%m/%d')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    changelogs = models.TextField()
    documentation = models.TextField()

    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, editable=False, blank=True, null = True)


    def __str__(self):
        return f' {self.mod} v.{self.version}'

    class Meta:
        unique_together = 'mod', 'version'


class Download(models.Model):
    mod_version = models.ForeignKey('ModVersion', on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.mod_version

    class Meta:
        pass
