from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'app.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^home/$', 'blog.views.home'),
                       # show a particular article
                       url(r'^article/(?P<id_article>\d+)/(?P<slug>.+)/$',
                           'blog.views.view_article'),
                       url(r'^register/$', 'blog.views.register'),
                       url(r'^confirmation/(?P<key>.+)/$',
                           'blog.views.confirmation'),
                       )
