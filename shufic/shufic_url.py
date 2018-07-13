from django.urls import re_path
from shufic.views import showvideo, hello, addlikes, onevideo, addcomment


urlpatterns = [
    re_path(r'^$', showvideo),
    re_path(r'^addlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'^Vaddlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'^onevideo/(?P<video_id>\d+)/$', onevideo),
    re_path(r'^addcomment/(?P<video_id>\d+)/$', addcomment),
]