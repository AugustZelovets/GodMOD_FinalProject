# Generated by Django 4.0.6 on 2022-07-24 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('genre', models.CharField(max_length=30)),
                ('team', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('description', models.CharField(max_length=255)),
                ('category', models.ForeignKey(default='SET_CATEGORY', on_delete=django.db.models.deletion.SET_DEFAULT, to='mod.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.game')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ModVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='1.0', max_length=10)),
                ('files', models.FileField(upload_to='')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('changelogs', models.TextField()),
                ('documentation', models.TextField()),
                ('mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.mod')),
            ],
        ),
        migrations.AddField(
            model_name='mod',
            name='tag',
            field=models.ManyToManyField(blank=True, to='mod.tag'),
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('mod_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.modversion')),
            ],
        ),
    ]