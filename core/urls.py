from django.conf.urls import url
from core.views import index, login, logout, signup, profile

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^signup/$', signup),
    url(r'^profile/$', profile),
]
