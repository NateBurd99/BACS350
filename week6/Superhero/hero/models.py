from django.db import models
from django.urls.base import reverse_lazy


class hero(models.Model):
    name = models.CharField(max_length=100, default = 'No Name')
    identity = models.CharField(max_length=100, default = 'Who is this??')
    description = models.TextField(default = 'Nothing to describe')
    strengths = models.TextField(max_length=100, default = 'No Strengths? Not much of a Superhero')
    weakness = models.TextField(max_length=100, default = 'no Weaknesses?')
    image = models.CharField(max_length=200, default = '/static/unknown.png')

    def __str__(self):
        return f'{self.name} : {self.description}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])
