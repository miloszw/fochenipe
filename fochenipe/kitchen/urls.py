from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^add/(\w+)/$', 'kitchen.views.add', name='kitchen_add'),
    url(r'^add/(\w+)/(\d+)$', 'kitchen.views.add', name='kitchen_add'),
    url(r'^select/(\d+)/$', 'kitchen.views.select', name='kitchen_select'),
)
