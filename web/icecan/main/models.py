from django.db import models

from django.utils.translation import ugettext_lazy as _

from icecan.authentication.models import User
from django.conf import settings
from django.db.models.signals import pre_save

# Create your models here.

CHAR_FIELD_TITLE_MAX_LENGTH = 128
CHAR_FIELD_VERSION_MAX_LENGTH = 16 # e.g. 10.0.1234 beta

class Atom(models.Model):
    pass

class Document(Atom):
    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')
    title = models.CharField(_('title'), max_length=CHAR_FIELD_TITLE_MAX_LENGTH)
    version = models.CharField(_('version number'), max_length=CHAR_FIELD_VERSION_MAX_LENGTH, blank=True, null=True)
    previous = models.ForeignKey('Document', null=True, blank=True)
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='document_created_by', null=True, editable=False)
    modified_by = models.ForeignKey(User, related_name='document_modified_by', null=True, editable=False)
    active = models.BooleanField(default=True)

class OriginalText(models.Model):
    text = models.TextField()
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='en')
    document = models.ForeignKey('Document')

class Chapter(Atom):
    class Meta:
        verbose_name = _('chapter')
        verbose_name_plural = _('chapters')
    title = models.CharField(_('title'), max_length=CHAR_FIELD_TITLE_MAX_LENGTH, null=True, blank=True)
    document = models.ForeignKey('Document', verbose_name=_('document'))

class Article(Atom):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
    chapter = models.ForeignKey('Document', verbose_name=_('document'))
    title = models.CharField(_('title'), max_length=CHAR_FIELD_TITLE_MAX_LENGTH, null=True, blank=True)
    text = models.TextField(_('text'), blank=True, default='')
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='en')

class Annotation(models.Model):
    text = models.ForeignKey('Atom')
    citation_start = models.IntegerField(null=True, blank=True)
    citation_end = models.IntegerField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)
    active = models.BooleanField(default=True)
