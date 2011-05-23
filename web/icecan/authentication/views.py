
from icecan.util import Response
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def settings(request):
    r = Response(request)
    
    return render_to_response('base.html', r)
