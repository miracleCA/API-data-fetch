from django.db import models

class Crypto(models.Model):
    cryptocurrency = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.cryptocurrency