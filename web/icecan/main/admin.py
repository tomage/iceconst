

from django.contrib import admin
from django.conf import settings
#from django.utils.translation import ugettext, ugettext_lazy as _

from models import Atom, Document, Text, Section, Article
from icecan.authentication.models import User
from django import forms
from icecan.main.widgets import DocumentActionsWidget



class DocumentAdminForm(forms.ModelForm):
    actions = forms.CharField(required=False, widget=DocumentActionsWidget())
    class Meta:
        model = Document
    class Media:
        js = (
          '/static/design/jquery.js',
          '/static/functional/document.js',
          )

class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
    list_display = ['title', 'version', 'previous', 'created_by', 'created', 'modified_by', 'modified', 'active']
    list_filter = ['active']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = User.objects.get(id=request.user.id)
        obj.modified_by = User.objects.get(id=request.user.id)
        obj.save()


admin.site.register(Document, DocumentAdmin)
admin.site.register(Text)
admin.site.register(Section)
admin.site.register(Article)
admin.site.register(Atom)
