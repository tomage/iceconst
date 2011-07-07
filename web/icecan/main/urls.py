from django.conf.urls.defaults import *

urlpatterns = patterns('icecan.main.views',
    # Main app
    (r'^$', 'main'),
    

    (r'^diff/$', 'diff'),

    (r'^documents/$', 'documents'),
    
    
    (r'^test/$', 'test'),
)

# Add some "main"-app admin urls
urlpatterns += patterns('icecan.main.admin_views',
    # Main app
    (r'^admin/main/generate_submodels/$', 'generate_submodels'),
    (r'^admin/main/generate_translations/$', 'generate_translations'),
)
