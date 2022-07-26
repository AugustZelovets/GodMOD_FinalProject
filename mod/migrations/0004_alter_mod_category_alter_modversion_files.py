# Generated by Django 4.0.6 on 2022-07-27 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mod.category'),
        ),
        migrations.AlterField(
            model_name='modversion',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
