# Generated by Django 4.0.6 on 2022-07-24 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now=True)),
                ('text', models.TextField()),
                ('published', models.BooleanField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mod.mod')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now=True)),
                ('mod_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.modversion')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('is_public', models.BooleanField()),
                ('mods', models.ManyToManyField(to='mod.mod')),
            ],
        ),
    ]
