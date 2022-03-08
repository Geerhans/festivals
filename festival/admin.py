from django.contrib import admin

from festival.models import Country, Story, Festival, Comment
# Register your models here.


admin.site.register(Country)
admin.site.register(Story)
admin.site.register(Festival)
admin.site.register(Comment)

