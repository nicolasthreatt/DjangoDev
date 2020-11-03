from django.db import models

class Stat(models.Model):
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.choice

class Player(models.Model):
    player = models.CharField(max_length=100)

    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
    

