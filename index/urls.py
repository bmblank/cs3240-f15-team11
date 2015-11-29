from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^register/$', views.Register),
    url(r'^report/(?P<report_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/create/$', views.create, name="create"),
    url(r'^report/$', views.ReportList, name="report_list"),
    url(r'^givepermissions/$', views.GivePermissions, name="give_permissions"),
    url(r'^report/(?P<report_id>[0-9]+)/edit/$', views.EditReport, name="edit_report"),
    url(r'^report/(?P<report_id>[0-9]+)/delete/$', views.DeleteReport, name="delete_report"),
    url(r'^report/(?P<report_id>[0-9]+)/removefromfolder$', views.RemoveReportFromFolder, name="remove_from_folder"),
    url(r'^suspension/$', views.Suspension, name='suspension'),
    url(r'^yourreports/$', views.YourReports, name="your_reports"),
    url(r'^yourreports/createfolder/$', views.CreateFolder, name="create_folder"),
    url(r'^yourreports/folder/(?P<folder_id>[0-9]+)/$', views.FolderDetails, name='folder_details'),
    url(r'^yourreports/folder/(?P<folder_id>[0-9]+)/removefolder$', views.RemoveFolder, name='remove_folder'),
    url(r'^yourreports/folder/(?P<folder_id>[0-9]+)/rename$', views.RenameFolder, name='rename_folder'),
    url(r'^yourreports/folder/(?P<folder_id>[0-9]+)/delete_folder_reports$', views.DeleteReportsInFolder, name='delete_folder_reports'), 
    url(r'^search/$', views.search, name='search'),

]