# Generated by Django 3.1.5 on 2021-01-25 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20210125_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='r_instructions',
            new_name='instructions',
        ),
    ]
