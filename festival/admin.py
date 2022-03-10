from django.contrib import admin


from festival.models import Country, Story, Festival, Comment
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('countryname',)}

admin.site.register(Country, CategoryAdmin)
admin.site.register(Story)
admin.site.register(Festival)
admin.site.register(Comment)


