from icecan.main.models import Text, Section, Article

import yaml
from pprint import pprint

def render_models_for_document(doc):
    """
    Parse the original text (assumed in YAML format) for a
    certain document and create sections and articles.
    If they exist beforehand, we dont override them.
    We do this for every original text found for the document
    (i.e. every language)
    
    Raises exception on error
    """
    original_texts = OriginalText.objects.filter(document=doc)
    for ot in original_texts:
        parsed = yaml.load(ot.text)
        pprint(parsed.keys())
        for section_title,section_contents in parsed.iteritems():
            # We only need to check whether the section exists - if so, we assume
            # the articles to exist also
            try:
                Section.objects.get(document=doc, title=section_title, language=ot.language)
                continue
            except: pass
            s = Section(document=doc, title=section_title, language=ot.language)
            s.save()
            if section_contents:
                for article_title,article_contents in section_contents.iteritems():
                    a = Article(section=s, title=article_title, text=article_contents, language=ot.language)
                    a.save()

def google_translate_text(text):
    """
    Throws the text at google translation API

    Raises exception on error
    """
    return "TRANSLATION"
