# Generated by Django 3.0.2 on 2020-03-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_data_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='username',
            field=models.CharField(default='hey', max_length=20),
        ),
    ]
