from django.contrib import admin
from django.db import models
from gnt_questionnaire.models import *
from cms.admin.placeholderadmin import PlaceholderAdmin

import settings








class QuestionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('titolo',)
        }),
        ('Pubblicazione', {
            'fields': ('slug','published')
        }),
    )
    class Media:
        js = ("http://code.jquery.com/jquery-1.6.2.min.js","/static/gnt_questionnaire/js/gnt_horizontal_edit.js",)
    prepopulated_fields = {"slug": ("titolo",)}
    list_display = ('titolo','published',)





class RispostaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('tipo','risposta','opzioni',)
        }),
        ('Pubblicazione', {
            'fields': ('published',)
        }),
    )
    class Media:
        js = ("http://code.jquery.com/jquery-1.6.2.min.js",)
    filter_horizontal=["opzioni"]


class DomandaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('questionario',)
        }), 
        (None, {
            'fields': ('tipo','multiple','domanda',)
        }),
        ('Pubblicazione', {
            'fields': ('numero','published','slug',)
        }),
    )
    class Media:
        js = ("http://code.jquery.com/jquery-1.6.2.min.js","/static/gnt_questionnaire/js/gnt_horizontal_edit.js",)

    prepopulated_fields = {"slug": ("domanda",)}
    list_display = ('slug',)


class rispApertaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('domanda','published',)
        }),
    )

    def has_add_permission(self, request):
        return False


admin.site.register(Questionario,QuestionarioAdmin)
admin.site.register(Domanda,DomandaAdmin)
admin.site.register(Risposta_aperta,rispApertaAdmin)
admin.site.register(Range)
admin.site.register(Risposta_chiusa)
