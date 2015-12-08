from django.contrib import admin

from .models import Report, Folder


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'Short_Description', 'Location_of_Event', 'created', 'author', 'folder_name_as_string','Attachment_is_Encrypted', 'group_name')

class FolderAdmin(admin.ModelAdmin):
    list_display = ('Folder_Name', 'creator')


admin.site.register(Report, ReportAdmin)
admin.site.register(Folder, FolderAdmin)
