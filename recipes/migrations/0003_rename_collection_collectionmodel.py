# Generated by Django 5.1.3 on 2024-12-28 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_collection'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collection',
            new_name='CollectionModel',
        ),
    ]