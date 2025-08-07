from django.db import models
from django.conf import settings

class Balancete(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome