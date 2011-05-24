from django.db import models

from django.utils.translation import ugettext_lazy as _

from icecan.authentication.models import User
from django.conf import settings

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
    def __unicode__(self):
        return '%s (ver. %s)' % (self.title, self.version)
    @property
    def sections(self):
        return Section.objects.filter(document=self)

class OriginalText(models.Model):
    text = models.TextField()
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='en')
    document = models.ForeignKey('Document')

class Section(Atom):
    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
    title = models.CharField(_('title'), max_length=CHAR_FIELD_TITLE_MAX_LENGTH, null=True, blank=True)
    document = models.ForeignKey('Document', verbose_name=_('document'))
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='en')
    def __unicode__(self):
        return '%s (%s)' % (self.title or 'Article of %s' % self.document, self.language)
    def articles(self):
        return Article.objects.filter(section=self)

class Article(Atom):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
    section = models.ForeignKey('Section', verbose_name=_('section'))
    title = models.CharField(_('title'), max_length=CHAR_FIELD_TITLE_MAX_LENGTH, null=True, blank=True)
    text = models.TextField(_('text'), blank=True, default='')
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='en')
    def __unicode__(self):
        return '%s (%s)' % (self.title or 'Article (excerpt: "%s..."' % self.text[:10], self.language)

class Annotation(models.Model):
    text = models.ForeignKey('Atom')
    citation_start = models.IntegerField(null=True, blank=True)
    citation_end = models.IntegerField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)
    active = models.BooleanField(default=True)
