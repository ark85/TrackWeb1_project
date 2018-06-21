from django.conf.urls import url
from answers.views import answer_details, answer_views, AnswerCreate, AnswerEdit
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<answer_id>\d+)/$', answer_details, name='answer_details'),
    url(r'^(?P<answer_id>\d+)/edit/$', login_required(AnswerEdit.as_view(pk_url_kwarg='answer_id')), name='answer_edit'),
    url(r'^create/$', AnswerCreate.as_view(), name='answer_create') #add login required
]
