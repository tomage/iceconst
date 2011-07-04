

from django.contrib import admin
from django.conf import settings
#from django.utils.translation import ugettext, ugettext_lazy as _

from models import Atom, Document, Text, Section, Article, Paragraph, Sentence, Phrase
from icecan.authentication.models import User
from django import forms
from icecan.main.widgets import TextActionsWidget



class TextAdminForm(forms.ModelForm):
    actions = forms.CharField(required=False, widget=TextActionsWidget())
    class Meta:
        model = Text

class TextAdmin(admin.ModelAdmin):
    form = TextAdminForm
    class Media:
        js = (
          '/static/design/jquery.js',
          '/static/functional/text.js',
          )
    
    """
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = User.objects.get(id=request.user.id)
        obj.modified_by = User.objects.get(id=request.user.id)
        obj.save()
    """

admin.site.register(Atom)
admin.site.register(Document)
admin.site.register(Text, TextAdmin)
admin.site.register(Section)
admin.site.register(Article)
admin.site.register(Paragraph)
admin.site.register(Sentence)
admin.site.register(Phrase)
