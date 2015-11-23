from django.contrib import admin

from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recepient', 'subject', 'body')


admin.site.register(Memo, MemoAdmin)