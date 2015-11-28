from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<memo_id>[0-9]+)/$', views.MemoDetails, name='memo_details'),
    url(r'^(?P<memo_id>[0-9]+)/delete/$', views.DeleteMemo, name='delete_memo'),
    url(r'^newmemos/$', views.NewMemo, name="create_memo"),
    url(r'^inbox/$', views.Inbox, name="inbox_list"),
]