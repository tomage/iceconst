#! -*- coding: utf-8 -*-

import re

class Response(dict):
    def __init__(self, request=None):
        self['lang'] = 'is' # may be overridden below
        self['template_base'] = 'base.html'
        
        if not request: return
        
        self['user'] = request.user
        if not request.user.is_authenticated():
            from django.contrib.auth.forms import AuthenticationForm
            self['login_form'] = AuthenticationForm(request)
            self['login_next'] = request.path

def add_response(view):
    def responsed_view(request, *args, **kwargs):
        r = Response(request)
        kwargs.update({'response': r})
        return view(request, *args, **kwargs)
    return responsed_view

def slugify(input):
    output = input.strip('_.- ').lower()
    # Letters    
    output = output.replace(u'á', 'a')
    output = output.replace(u'ð', 'd')
    output = output.replace(u'é', 'e')
    output = output.replace(u'í', 'i')
    output = output.replace(u'ó', 'o')
    output = output.replace(u'ú', 'u')
    output = output.replace(u'ý', 'y')
    output = output.replace(u'þ', 'th')
    output = output.replace(u'æ', 'ae')
    output = output.replace(u'ö', 'o')
    # text
    output = output.replace('&', 'og') 
    output = output.replace('/', '_')
    # commas
    output = output.replace(',', '_')

    output = output.rstrip()
    # special chars
    output = re.sub('\s+', '_', output)
    output = re.sub('[^\w.-]', '', output)

    # squash underscores
    while '__' in output:
        output = output.replace('__', '_')

    return output

