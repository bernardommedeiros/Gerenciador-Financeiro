from django.db import models
from django.conf import settings

class Balancete(models.Model):
    
    user = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name='balancetes'
     )
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']