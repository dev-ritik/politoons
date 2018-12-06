from django.contrib import admin

from myapp.models import Politoon


class PolitoonAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'party', 'majorRole')


admin.site.register(Politoon, PolitoonAdmin)
