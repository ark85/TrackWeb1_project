from django.conf.urls import url
from categories.views import category_details, category_views

urlpatterns = [
    url(r'^$', category_views, name='categories'),
    url(r'^(?P<category_id>\d+)/$', category_details, name='category_details')
]
