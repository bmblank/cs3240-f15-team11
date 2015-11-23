from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^message/$', views.MessageList),
    url(r'^about/$', views.About),
    url(r'^mission/$', views.Mission),
    url(r'^security/$', views.Security),
    url(r'^contact/$', views.Contact),
    url(r'^report/(?P<report_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/create/$', views.create, name="create"),
    url(r'^report/$', views.ReportList),

]