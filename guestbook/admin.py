from django.contrib import admin
from models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    date_hierarchy = 'posted'
    list_display = ['posted', 'user', 'content']
    list_display_links = ['posted']
    list_filter = ['user', 'posted']
    preserve_filters = False
    list_per_page = 5
    list_max_show_all = 50
    list_editable = ['content']
    search_fields = ['user', 'content']
    ordering = ['user', 'posted']

    # fields = ['content']
    # exclude = ['user']
    # readonly_fields = ['posted']

    save_as = False
    save_on_top = True

    fieldsets = [
        ['dd', {
            'classes': ['collapse'],
            'fields': ['user'],
        }],
        ['ww', {
            'fields': ['content']
        }],
    ]


admin.site.register(Guestbook, GuestbookAdmin)
