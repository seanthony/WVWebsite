# Generated by Django 3.0.5 on 2020-04-20 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_ordinance'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordinance',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
