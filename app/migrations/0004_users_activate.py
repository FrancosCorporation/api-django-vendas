# Generated by Django 3.1.2 on 2020-11-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201101_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='activate',
            field=models.BooleanField(auto_created=True, default=False),
        ),
    ]
