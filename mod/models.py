from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField()
    genre = models.CharField(max_length=30)
    team = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        pass


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        pass


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Mod(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='MainModImages/%Y/%m/%d')

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False )

    author = models.CharField(max_length=30)
    tag = models.ManyToManyField(Tag, blank=True)
    likes = models.IntegerField(default=0, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        pass


class ModVersion(models.Model):
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE)
    version = models.CharField(max_length=10, default='1.0', )
    files = models.FileField(null=True, blank=True, upload_to='ModFiles/%Y/%m/%d')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    changelogs = models.TextField()
    documentation = models.TextField()

    def __str__(self):
        return f' {self.mod} v.{self.version}'

    class Meta:
        pass


class Download(models.Model):
    mod_version = models.ForeignKey(ModVersion, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.mod_version

    class Meta:
        pass
