from django.contrib import admin
from .models import Concert, Producer, Setlist, Song, VOCALOID

# Register your models here.
admin.site.register(Concert)
admin.site.register(Producer)
admin.site.register(Setlist)
admin.site.register(Song)
admin.site.register(VOCALOID)