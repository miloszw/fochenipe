from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.home', name='recipe_home'),
    url(r'^add/$', 'recipe.views.add', name='recipe_add'),
)
