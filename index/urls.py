from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home', views.Home),
    url(r'^report/$', views.ReportList, name="report_list"),
    url(r'^report/(?P<report_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/create/$', views.create, name="create"),
    url(r'^message/$', views.Message),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^about/$', views.GettingStarted),
    url(r'^mission/$', views.Mission),
    url(r'^security/$', views.Security),
    url(r'^contact/$', views.Contact),
    url(r'^register/$', views.Register),
    url(r'^givepermissions/$', views.GivePermissions, name="give_permissions"),

]