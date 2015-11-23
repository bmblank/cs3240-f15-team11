from django.contrib import admin

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'Short_Description', 'Location_of_Event', 'sensitivity', 'created', 'author')


admin.site.register(Report, ReportAdmin)