from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Hackathon)
admin.site.register(Team)
admin.site.register(Announcement)
admin.site.register(Round)
admin.site.register(Organizer)
admin.site.register(Statistics)