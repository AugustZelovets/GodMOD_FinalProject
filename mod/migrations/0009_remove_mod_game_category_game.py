# Generated by Django 4.0.6 on 2022-08-05 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0008_category_slug_game_slug_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod',
            name='game',
        ),
        migrations.AddField(
            model_name='category',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mod.game'),
            preserve_default=False,
        ),
    ]