# Generated by Django 4.0.6 on 2022-07-26 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_page_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='comment',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='page.comment'),
        ),
    ]
