from ..models.boleto import Boleto
from ..models.balancete import Balancete
from django.db.models import Sum

def criar_boleto(data, files, balancete_id):
    balancete = Balancete.objects.get(id=balancete_id)
    
    novo_boleto = Boleto(
        title=data.get('title'),
        value=data.get('value'),
        category=data.get('category'),
        boleto_img=files.get('boleto_img') if files else None,
        balancete=balancete
    )
    novo_boleto.save()
    return novo_boleto

def listar_boletos(balancete_id=None):
    if balancete_id:
        return Boleto.objects.filter(balancete_id=balancete_id)
    return Boleto.objects.all()

def calcular_saldo(balancete_id=None):
    obj = Boleto.objects
    if balancete_id:
        obj = obj.filter(balancete_id=balancete_id)
    faturamento = obj.filter(category="Faturamento").aggregate(total=Sum('value'))['total'] or 0
    despesa = obj.filter(category="Despesa").aggregate(total=Sum('value'))['total'] or 0
    saldo = faturamento - despesa
    return {
        'saldo': saldo,
        'faturamento': faturamento,
        'despesa': despesa
    }
    
def boleto_delete(boleto_id):
    boleto = Boleto.objects.get(id=boleto_id)
    boleto.delete()
    return True

def boleto_update(boleto_id, data, files):
    boleto = Boleto.objects.get(id=boleto_id)
    boleto.title = data.get('title', boleto.title)
    boleto.value = data.get('value', boleto.value)
    boleto.category = data.get('category', boleto.category)
    if files and 'boleto_img' in files:
        boleto.boleto_img = files.get('boleto_img')
    boleto.save()
    return boleto