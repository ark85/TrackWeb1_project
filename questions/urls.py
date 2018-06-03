from django.conf.urls import url
from questions.views import question_details, question_views
from questions.views import QuestionEdit, QuestionCreate

urlpatterns = [
    url(r'^$', question_views, name='questions'),
    url(r'^(?P<question_id>\d+)/$', question_details, name='question_details'),
    url(r'^(?P<question_id>\d+)/edit/$', QuestionEdit.as_view(pk_url_kwarg='question_id'), name='question_edit'),
    url(r'^create/$', QuestionCreate.as_view(), name='question_create'),
    # login_required it is undesirable to use, add this decorator into the location of the view -- Done
]