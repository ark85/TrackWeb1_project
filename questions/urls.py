from django.conf.urls import url
from questions.views import question_details, question_views
from questions.views import QuestionEdit, QuestionCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', question_views, name='questions'),
    url(r'^(?P<question_id>\d+)/$', question_details, name='question_details'),
    url(r'^(?P<question_id>\d+)/edit/$', login_required(QuestionEdit.as_view(pk_url_kwarg='question_id')), name='question_edit'),
    url(r'^create/$', login_required(QuestionCreate.as_view()), name='question_create'),
]