from django.conf.urls import url
from questions.views import question_details, question_views

urlpatterns = [
    url(r'^$', question_views, name='questions'),
    url(r'^(?P<question_id>\d+)/$', question_details, name='question_details')
]