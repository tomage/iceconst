# Create your views here.

from django.shortcuts import render_to_response

from icecan.util import add_response
from icecan.main.models import Document

@add_response
def main(request, response):
    
    # Get latest document for front page...
    doc = Document.objects.filter().order_by('-modified')[0]
    response['doc'] = doc
    
    return render_to_response('main/base.html', response)
