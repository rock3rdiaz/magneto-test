# Generated by Django 3.2.4 on 2021-06-19 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='adn',
            new_name='dna',
        ),
    ]