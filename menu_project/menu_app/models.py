from django.db import models

class FoodIngredient(models.Model):
    name = models.CharField(max_length=100)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(FoodIngredient)
