# Generated by Django 3.2.3 on 2021-09-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_remove_solarsystem_nebula background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nebula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name of Nebula', models.CharField(max_length=100)),
            ],
        ),
    ]
