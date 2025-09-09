from ..models.balancete import Balancete

def criar_balancete(user, data):
    return Balancete.objects.create(
        user=user,
        title=data.get('title'),
        description=data.get('description', '')
    )

def listar_balancetes():
    return Balancete.objects.all()

def balancete_delete(balancete_id):
    balancete = Balancete.objects.get(id=balancete_id)
    balancete.delete()
    return True

def balancete_update(balancete_id, data):
    balancete = Balancete.objects.get(id=balancete_id)
    balancete.title = data.get('title', balancete.title)
    balancete.description = data.get('description', balancete.description)
    balancete.save()
    return balancete