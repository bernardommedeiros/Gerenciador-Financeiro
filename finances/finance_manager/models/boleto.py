from django.db import models
from django.conf import settings 
from django.core.exceptions import ValidationError

class Boleto(models.Model):
    CATEGORIES = [
        ('Faturamento', 'Faturamento'),
        ('Despesa', 'Despesa'),
    ]
    
    title = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='Despesa')
    date = models.DateField(auto_now_add=True)
    boleto_img = models.ImageField(upload_to='boletos/', blank=True, null=True)
    balancete = models.ForeignKey(
        'personal_finance.Balancete',
        on_delete=models.CASCADE,
        related_name='boletos',
        null=True,
    )
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.value} ({self.category})"
    
    def clean(self):
        if self.value < 0:
            raise ValidationError({'value': "Valor inválido, indique um valor positivo."})
        
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)