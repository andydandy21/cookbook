# Generated by Django 3.1.5 on 2021-01-21 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210121_1114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeTags',
        ),
    ]