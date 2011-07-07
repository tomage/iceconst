from icecan.main.models import Text, Section, Article, Paragraph, Sentence, Word

from yaml import load, dump
try:
        from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from pprint import pprint
from icecan.util import slugify

def isnumeric(value):
    return str(value).replace(".","").replace("-","").isdigit()

def render_models_for_text(text):
    """
    Parse the original text (assumed in YAML format) for a
    certain text and create sections, articles, etc.
    We delete all objects previously derived.
    """
    if isnumeric(text):
        text = Text.objects.get(id=text)
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
                                    sen_tmp = sen.replace(',', ' ,')
                                    for word in sen.split(' '):
                                        word = word.strip()
                                        if word:
                                            w = Word(sentence=se, title=word[:50], raw_buffer=word)
                                            w.slug = slugify(word[:50])
                                            w.save()

def google_translate_text(text):
    """
    Throws the text at google translation API

    Raises exception on error
    """
    return "TRANSLATION"

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Do some console text work.')
    parser.add_argument('--generate-submodels-for-all-texts', const=True, action='store_const')
    args = parser.parse_args()
    
    if args.generate_submodels_for_all_texts:
        for t in Text.objects.all():
            render_models_for_text(t)
