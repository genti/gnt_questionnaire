from django.db.models.signals import post_save, m2m_changed,pre_save
from django.dispatch import receiver
from models import *

import logging

@receiver(post_save, sender=Domanda)
def manage_domanda_type(sender, **kwargs):
    domanda = kwargs.get("instance", None)
    created = kwargs.get("created", None)
    if created:
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
        
        
# @receiver(post_save, sender=CustomerContact)
# def log_new_customer_contact(sender, **kwargs):
#     cc = kwargs.get("instance", None)
#     created = kwargs.get("created", None)
# #     if created:
# #         logging.getLogger('contacts').debug("new customer contact: %s on %s" % (cc.contact.email, cc.customer.name))
#         
# @receiver(post_save, sender=ContactMailingStatus)
# def log_new_contact_mailing_status(sender, **kwargs):
#     cms = kwargs.get("instance", None)
#     created = kwargs.get("created", None)
# #     if created:
# #         logging.getLogger('sending').debug("new status for nl %s: %s %s" % (cms.newsletter.slug, cms.contact.email, cms.status ))