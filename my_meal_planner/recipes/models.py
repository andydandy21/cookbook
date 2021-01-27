from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    description = models.TextField(max_length=500, default="Add a description!")
    image = models.ImageField(default='default.png', upload_to='recipe_pics')
    tags = models.ManyToManyField(Tag, null=True)
    instructions = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk':self.pk})    

class Ingredient(models.Model):
    MEASUREMENT_CHOICES = [
        ('UNIT','unit'),
        ('TEASPOON', 'tsp'),
        ('TABLESPOON','tbsp'),
        ('FLUID_OUNCE','fl oz'),
        ('CUP','cup'),
        ('PINT','pt'),
        ('QUART','qt'),
        ('GALLON','gal'),
        ('MILLILITER','mL'),
        ('LITER','L'),
        ('DECILITER','dL'),
        ('POUND','lb'),
        ('OUNCE','oz'),
        ('MILLIGRAM','mg'),
        ('GRAM','g'),
        ('KILOGRAM','kg')
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    measurement = models.CharField(max_length=11, choices=MEASUREMENT_CHOICES, default='UNIT')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.quantity) + ' ' + self.measurement + ' of ' + self.name


