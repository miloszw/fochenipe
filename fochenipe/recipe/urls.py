from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.home', name='recipe_home'),
    url(r'^add/$', 'recipe.views.add', name='recipe_add'),
    url(r'^(\d+)$', 'recipe.views.detail', name='recipe_detail'),
    url(r'^(\d+)/make$', 'recipe.views.make', name='recipe_make'),
    url(r'^(\d+)/delete$', 'recipe.views.delete', name='recipe_del'),
)
