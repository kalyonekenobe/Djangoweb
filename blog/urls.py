from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.post_list, name='post_list'),
    url('^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url('^post/create/$', views.create_post, name='create_post'),
    url('^post/(?P<pk>[0-9]+)/edit/$', views.edit_post, name='edit_post'),
    url('^post/drafts/(?P<user_id>[0-9]+)/$', views.post_draft_list, name='post_draft_list'),
    url('^post/(?P<pk>[0-9]+)/publish/$', views.publish_post, name='publish_post'),
    url('^post/(?P<pk>[0-9]+)/remove/$', views.remove_post, name='remove_post'),

]