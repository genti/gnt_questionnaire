from django.contrib import admin
from django.db import models
from gnt_questionnaire.models import *
from cms.admin.placeholderadmin import PlaceholderAdmin
from django.utils.html import strip_tags

import settings








class QuestionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('titolo','intro','long_intro',)
        }),
        ('Pubblicazione', {
            'fields': ('slug','published')
        }),
    )
    class Media:
        js = ("http://code.jquery.com/jquery-1.6.2.min.js","/static/cms/wymeditor/jquery.wymeditor.js","/static/cms/wymeditor/plugins/resizable/jquery.wymeditor.resizable.js","/static/localsite/js/rich.js",)

    prepopulated_fields = {"slug": ("titolo",)}
    list_display = ('titolo','published',)




class DomandaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('questionario',)
        }), 
        (None, {
            'fields': ('tipo','multiple','domanda',)
        }),
        ('Pubblicazione', {
            'fields': ('numero','published',)
        }),
    )
    
    def domanda_view(self):
        return '<b>%s</b> , %s' % (self.questionario.titolo,strip_tags(self.domanda))
    domanda_view.short_description = 'Questionario, domanda'
    domanda_view.allow_tags = True
    
    
    class Media:
        js = ("http://code.jquery.com/jquery-1.6.2.min.js","/static/cms/wymeditor/jquery.wymeditor.js","/static/cms/wymeditor/plugins/resizable/jquery.wymeditor.resizable.js","/static/localsite/js/rich.js",)
    list_display = ('numero',domanda_view,)
    list_filter = ('questionario','tipo',)




class rispApertaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('domanda','maxlength','published',)
        }),
    )
    list_filter = ('domanda__questionario',)

    def has_add_permission(self, request):
        return False

class rispChiusaAdmin(admin.ModelAdmin):
    list_filter = ('domanda__questionario','domanda',)

admin.site.register(Questionario,QuestionarioAdmin)
admin.site.register(Domanda,DomandaAdmin)
admin.site.register(Risposta_aperta,rispApertaAdmin)
admin.site.register(Range)
admin.site.register(Risposta_chiusa,rispChiusaAdmin)
