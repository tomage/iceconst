# Create your views here.

from django.shortcuts import render_to_response

from icecan.util import add_response

@add_response
def main(request, response):
    return render_to_response('main/base.html', response)
