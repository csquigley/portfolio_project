from django.contrib import admin
from .models import *

admin.site.register(Resume)

class SubsectionInline(admin.TabularInline):
    model = ProjectSection 

class ResumeSectionObjectInline(admin.TabularInline):
    model = ResumeSectionObject

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [SubsectionInline]
# Register your models here.

@admin.register(ResumeSection)
class ResumeSectionAdmin(admin.ModelAdmin):
    inlines = [ResumeSectionObjectInline]

