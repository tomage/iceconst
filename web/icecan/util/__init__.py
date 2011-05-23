
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
