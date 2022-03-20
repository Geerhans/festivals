from django.contrib import admin

from festival.models import UserProfile
from festival.models import Country,Festival
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('countryname',)}

admin.site.register(Country, CategoryAdmin)

admin.site.register(Festival)

admin.site.register(UserProfile)


