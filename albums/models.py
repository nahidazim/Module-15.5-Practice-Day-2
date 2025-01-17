from django.db import models
from musicians.models import Musician

class Album(models.Model):
    name = models.CharField(max_length=100)
    musicians = models.ManyToManyField(Musician)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name
