# Generated by Django 3.0.2 on 2020-03-10 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200308_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
