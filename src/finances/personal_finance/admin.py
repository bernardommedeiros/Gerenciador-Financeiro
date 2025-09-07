from django.contrib import admin
from .models.user import User
from .models.balancete import Balancete
from .models.boleto import Boleto

admin.site.register(User)
admin.site.register(Balancete)
admin.site.register(Boleto)