# Create your views here.

from django.shortcuts import render_to_response

from icecan.util import add_response
from icecan.main.models import Document

@add_response
def main(request, response):
    # Get latest documents for front page
#    response['doc'] = Document.objects.filter().order_by('-modified')[0]
#    response['prevdoc'] = Document.objects.filter().order_by('-modified')[1]
    return render_to_response('main/base.html', response)

@add_response
def diff(request, response):
    """For now, just compares two latest created documents"""
    r = response

    # Fetch the documents in question
    docA, docB = Document.objects.all().order_by('-created')[:2]
    r['docA'] = docA
    r['docB'] = docB

    # Create article comparisons
    article_comparisons = []
    for articleA in docA.articles:
        for articleB in docB.articles:
            if articleB.slug != articleA.slug:
                continue
            break
    r['article_comparisons'] = article_comparisons

    r['oldText'] = """A text, within literary theory, is a coherent set of symbols that transmits some kind of informative message.
This set of symbols is conidered in terms of the infomative message's content, rather than in terms of its physical form or the medium in which it is represented. In the most basic terms established by structuralist criticism,
therefore, a "text" is any object that can be "read,"
whether this object is a
work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing."""
    r['newText'] = """A text, within literary theory, is the coherent set of symbs that transmits some kind of informative message.
This set of in terms of the informative message's content, symbols rather than in terms of its physical form or the medium in which it is represented. In the most basic terms established by structuralist criticism,
therefore, a "text" is any object that can be "read,"

whether is a
whether is a
work of literature, new text here a street sign, an interesting arrangement of buildings on a city block, or styles of clothing."""

    return render_to_response('main/diff.html', response)

@add_response
def documents(request, response):
    response['documents'] = Document.objects.all()
    return render_to_response('main/documents.html', response)
