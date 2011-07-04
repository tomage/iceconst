from icecan.main.models import Text, Section, Article, Paragraph, Sentence

from yaml import load, dump
try:
        from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from pprint import pprint
from icecan.util import slugify

def render_models_for_text(text):
    """
    Parse the original text (assumed in YAML format) for a
    certain text and create sections, articles, etc.
    We delete all objects previously derived.
    """
    for section in text.sections:
        section.delete()
    parsed = load(text.original_text, Loader)
    pprint(parsed.keys())
    for section_title,section_contents in parsed.iteritems():
        s = Section(text=text, title=section_title)
        s.slug = slugify(s.title)
        s.save()
        if section_contents:
            for article_title,article_contents in section_contents.iteritems():
                article_title = article_title.strip()
                article_contents = article_contents.strip()
                if article_contents:
                    a = Article(section=s, title=article_title or '-')
                    a.slug = slugify(a.title)
                    a.save()
                    print '\n\n\nArticle:'
                    print article_contents
                    # Now split article into paragraphs
                    for par in article_contents.split('\n'):
                        par = par.strip()
                        if par:
                            p = Paragraph(article=a, title='P: %s...'%par[:7])
                            p.slug = slugify(p.title[:7])
                            p.save()
                            for sen in par.split('.'):
                                sen = sen.strip()
                                if sen:
                                    se = Sentence(paragraph=p, title='S: %s...'%sen[:7], raw_buffer=sen)
                                    se.slug = slugify(se.title[:7])
                                    se.save()

def google_translate_text(text):
    """
    Throws the text at google translation API

    Raises exception on error
    """
    return "TRANSLATION"
