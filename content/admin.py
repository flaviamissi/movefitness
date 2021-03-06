from django.contrib import admin

from content.models import Content


class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Content, ContentAdmin)
