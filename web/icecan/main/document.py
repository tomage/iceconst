from icecan.main.models import OriginalText


def render_models_for_document(doc):
    """
    Parse the original text for a certain document and create
    chapters and articles.
    If they exist beforehand, we dont override them.
    We do this for every original text found for the document
    (i.e. every language)
    
    Raises exception on error
    """
    original_texts = OriginalText.objects.filter(document=doc)
    for ot in original_texts:
        pass

def google_translate_text(text):
    """
    Throws the text at google translation API

    Raises exception on error
    """
    return "TRANSLATION"