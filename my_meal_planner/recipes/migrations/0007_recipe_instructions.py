# Generated by Django 3.1.5 on 2021-01-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20210124_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
