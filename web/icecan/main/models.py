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
    @property
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
    
    original_text = models.TextField(help_text=_(u'This is the text we convert to model objects'))
    language = models.CharField(_('language'), max_length=len('xx_XX'), choices=settings.LANGUAGES, default='is')

    @property
    def sections(self):
        return Section.objects.filter(text=self)


class Section(Atom):
    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
    
    text = models.ForeignKey('Text')
    
    @property
    def articles(self):
        return Article.objects.filter(section=self)



class Article(Atom):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
    
    section = models.ForeignKey('Section')
    
    def __unicode__(self):
        return self.title or u'Article (excerpt: "%s..."' % self.buffer[:10]
    @property
    def buffer(self):
        return u'<div id="%d" class="article">%s</div>' % (self.id, u' '.join(p.buffer for p in self.paragraphs))
    @property
    def paragraphs(self):
        return Paragraph.objects.filter(article=self)

class Paragraph(Atom):
    class Meta:
        verbose_name = _('paragraph')
        verbose_name_plural = _('paragraphs')

    article = models.ForeignKey('Article')
    
    def __unicode__(self):
        return self.title or u'Paragraph (excerpt: "%s..."' % self.buffer[:10]
    @property
    def buffer(self):
        return u'<p id="%d" class="paragraph">%s</p>' % (self.id, u' '.join(p.buffer for p in self.sentences))
    @property
    def sentences(self):
        return Sentence.objects.filter(paragraph=self)


class Sentence(Atom):
    class Meta:
        verbose_name = _('sentence')
        verbose_name_plural = _('sentences')

    paragraph = models.ForeignKey('Paragraph')
    
    raw_buffer = models.TextField()

    def __unicode__(self):
        return self.title or u'Sentence (excerpt: "%s..."' % self.buffer[:10]
    @property
    def buffer(self):
        return u'<span id="%d" class="sentence">%s</span>' % (self.id, self.raw_buffer)


class Phrase(Atom):
    class Meta:
        verbose_name = _('phrase')
        verbose_name_plural = _('phrases')

    article = models.ForeignKey('Article')
    
    from_char = models.IntegerField()
    to_char = models.IntegerField()

    TYPE_CHOICES = (
        ('NORMAL', 'Normal'),
        ('AMBIGUOUS', 'Ambiguous'),
        ('WEASEL', 'Weasel'),
    )
    type = models.CharField(max_length=max([len(C[0]) for C in TYPE_CHOICES]), choices=TYPE_CHOICES)

#
