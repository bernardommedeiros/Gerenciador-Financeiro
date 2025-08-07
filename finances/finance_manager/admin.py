from django.contrib import admin

# Register your models here.

from .models.user import User
from .models.boleto import Boleto
from .models.balancete import Balancete

admin.site.register(User)
admin.site.register(Boleto)
admin.site.register(Balancete)