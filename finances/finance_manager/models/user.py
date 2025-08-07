from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username
    
    def clean(self):
        errors = {}

        if self.name and len(self.name) <= 2:
            errors['name'] = "O nome deve possuir no mínimo 3 caracteres"

        if self.username and len(self.username) <= 2:
            errors['username'] = "O nome de usuário deve possuir no mínimo 3 caracteres"

        if self.username and not re.match(r'^[\w\sÀ-ÿ]+$', self.username):
            errors['username'] = "O nome do grupo não pode conter caracteres especiais."
      
        if errors:
            raise ValidationError(errors)


    def save(self, *args, **kwargs):

        self.full_clean()  
        super().save(*args, **kwargs)