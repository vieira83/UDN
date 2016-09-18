from django.contrib import admin
from udn.models import Participants


class ParticipantsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Participants, ParticipantsAdmin)