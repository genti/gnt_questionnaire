from django.db.models.signals import post_save, m2m_changed,pre_save
from django.dispatch import receiver
from models import *

import logging

@receiver(post_save, sender=Domanda)
def manage_domanda_type(sender, **kwargs):
    domanda = kwargs.get("instance", None)
    created = kwargs.get("created", None)
    if created:
        if domanda.tipo == '1':
            ra=Risposta_aperta(domanda=domanda)
            ra.save();   
        if domanda.tipo == '3':
            ra=Risposta_aperta(domanda=domanda)
            ra.save();   
           
@receiver(pre_save, sender=Domanda)
def manage_domanda_order(sender, **kwargs):
    domanda = kwargs.get("instance", None)
    created = kwargs.get("created", None)
    if not domanda.numero:
        domande=Domanda.objects.filter().order_by('-numero')[:1]
        if domande:
            domanda.numero=(int(domande[0].numero)+1)
        else:
            domanda.numero=0
        
        
# @receiver(post_save, sender=Risultati)
# def checkQuestionarioStatus(sender, **kwargs):
#     risultati_obj = kwargs.get("instance", None)
#     
#     for domanda in questionario.domanda_set.all():
#     
#         if domanda.tipo = 0:
#             totRisposteChiuse += len(domanda.risposta_chiusa_set.all())
#         
#         if domanda.tipo == 1
#             totRisposteAperte += len(domanda.risposta_aperta_set.all())
#         
#         if domanda.tipo == 2
#             totRisposteRange += 1
#             
#     
#     
#     TOTrisposte=totRisposteChiuse+totRisposteAperte+totRisposteRange
    
    


