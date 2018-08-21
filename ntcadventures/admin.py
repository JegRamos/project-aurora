from django.contrib import admin
from ntcadventures.models import Supervisor, OvertimeRequest, Entry, File


admin.site.register(Supervisor),
admin.site.register(OvertimeRequest),
admin.site.register(Entry),
admin.site.register(File)
