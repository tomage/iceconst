from django.db import models

from django.utils.translation import ugettext_lazy as _

from icecan.authentication.models import User
from django.conf import settings



CHAR_FIELD_TITLE_MAX_LENGTH = 128
CHAR_FIELD_VERSION_MAX_LENGTH = 16 # e.g. 10.0.1234 beta



class Atom(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_TITLE_MAX_LENGTH, blank=True, null=True)
    slug = models.SlugField(max_length=CHAR_FIELD_TITLE_MAX_LENGTH, blank=True, null=True)
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='document_created_by', null=True, editable=False)
    modified_by = models.ForeignKey(User, related_name='document_modified_by', null=True, editable=False)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title



class Document(Atom):
    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')
    version = models.CharField(_('version number'), max_length=CHAR_FIELD_VERSION_MAX_LENGTH, blank=True, null=True)
    previous = models.ForeignKey('Document', null=True, blank=True)
    
    def __unicode__(self):
        return '%s (ver. %s)' % (self.title, self.version)
    def texts(self):
        return Text.objects.filter(document=self)
    @property
    def articles(self):
        return Article.objects.filter(section__text__document=self)

class Text(Atom):
    class Meta:
        verbose_name = _('text')
        verbose_name_plural = _('texts')
    
    document = models.ForeignKey('Document')
    
    original_text = models.TextField()
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='is')

    def sections(self):
        return Section.objects.filter(text=self)


class Section(Atom):
    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
    
    text = models.ForeignKey('Text')
    
    def articles(self):
        return Article.objects.filter(section=self)



class Article(Atom):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
    
    section = models.ForeignKey('Section', verbose_name=_('section'))
    
    buffer = models.TextField(_('text'))
    
    def __unicode__(self):
        return self.title or u'Article (excerpt: "%s..."' % self.text[:10]

