from django.conf.urls import url
from categories.views import category_details, category_views, category_create, CategoryEdit
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', category_views, name='categories'),
    url(r'^(?P<category_id>\d+)/$', category_details, name='category_details'),
    url(r'^(?P<category_id>\d+)/edit/$', login_required(CategoryEdit.as_view(pk_url_kwarg='category_id')), name='category_edit'),
    url(r'^create/$', login_required(category_create), name='category_create'),
]
