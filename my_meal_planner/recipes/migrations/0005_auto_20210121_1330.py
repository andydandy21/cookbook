# Generated by Django 3.1.5 on 2021-01-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.png', upload_to='recipe_pics'),
        ),
    ]
