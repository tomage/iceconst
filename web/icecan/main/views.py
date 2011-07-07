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
    articles = []
    for articleA in docA.articles:
        for articleB in docB.articles:
            if articleB.slug != articleA.slug:
                continue
            articles.append({'articleA': articleA, 'articleB': articleB})
            break
    r['articles'] = articles

    return render_to_response('main/diff.html', response)

@add_response
def documents(request, response):
    response['documents'] = Document.objects.all()
    return render_to_response('main/documents.html', response)


@add_response
def test(request, response):
    return render_to_response('test.html', response)
