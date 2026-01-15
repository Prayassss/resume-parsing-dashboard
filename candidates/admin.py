from django.contrib import admin
from .models import Candidate, Project


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    search_fields = ("full_name", "email", "skills")
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "candidate")
