from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    rating = models.DecimalField(decimal_places=2,max_digits=10)
    genre = models.ManyToManyField('Genre',related_name="genre")

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name