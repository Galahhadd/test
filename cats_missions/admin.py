from django.contrib import admin

from .models import SpyCat, Mission, Target

@admin.register(SpyCat)
class SpyCatAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'years_of_experience', 'breed', 'salary')

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('id','cat', 'complete')

@admin.register(Target)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'country', 'notes', 'complete')



