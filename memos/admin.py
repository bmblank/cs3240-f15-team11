from django.contrib import admin

from .models import Memo, Key


class MemoAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'body', 'created', 'encrypted')

class KeyAdmin(admin.ModelAdmin):
    list_display = ('rKey', 'privateKey', 'publicKey')


admin.site.register(Memo, MemoAdmin)
admin.site.register(Key, KeyAdmin)