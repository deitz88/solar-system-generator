# Generated by Django 3.2.3 on 2021-09-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_nebula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nebula',
            name='Name of Nebula',
        ),
        migrations.AddField(
            model_name='nebula',
            name='Max',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='nebula',
            name='Min',
            field=models.IntegerField(default=15),
        ),
    ]
