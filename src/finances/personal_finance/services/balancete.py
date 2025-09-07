from ..models.balancete import Balancete

def criar_balancete(user, data):
    return Balancete.objects.create(
        user=user,
        title=data.get('title'),
        description=data.get('description', '')
    )

def listar_balancetes():
    return Balancete.objects.all()
