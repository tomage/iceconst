# Create your views here.

from django.shortcuts import render_to_response, HttpResponse
from models import Document
from django.conf import settings
from icecan.util import add_response
from icecan.main.document import render_models_for_document, google_translate_text
from icecan.main.models import Text
from django.http import HttpResponseServerError, HttpResponseBadRequest

@add_response
def generate_submodels(request, response):
    try:
        doc_id = int(request.GET.get('document_id'))
        doc = Document.objects.get(id=doc_id)
    except:
        return HttpResponseBadRequest('Please supply valid document id', mimetype='text/plain')
    
    render_models_for_document(doc)
    return HttpResponse('Submodel generation successful!', mimetype="text/plain")

@add_response
def generate_translations(request, response):
    try:
        doc_id = int(request.GET.get('document_id'))
        doc = Document.objects.get(id=doc_id)
    except:
        return HttpResponseBadRequest('Please supply valid document id', mimetype='text/plain')
    
    # Loop over langs and check if translations exist, if not, create them.
    # If any error occurs, we immediately return ServerError (should probably do sth. more sensible...(
    icelandic_text = OriginalText.objects.get(document=doc, language='en')
    for lang in settings.LANGUAGES:
        try:
            OriginalText.objects.get(document=doc, language=lang[0])
        except:
            ot = OriginalText(document=doc, language=lang[0])
            try:
                ot.text = google_translate_text(icelandic_text.text)
            except:
                return HttpResponseServerError('Could not translate via google...', mimetype='text/plain')
            #ot.save()
    
    return HttpResponse('Translation successful!', mimetype='text/plain')
