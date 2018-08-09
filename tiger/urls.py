from django.conf.urls import url
from tiger.views import head,legs

urlpatterns = [
    url(r'^$',head),
    url(r'^(?P<info_id>[0-9])/$',legs),
]