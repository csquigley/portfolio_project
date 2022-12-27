from django.contrib import admin
from .models import *

class SubsectionInline(admin.TabularInline):
    model = ProjectSection

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [SubsectionInline]
# Register your models here.
admin.site.register(Post)
