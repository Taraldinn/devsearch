from django.contrib import admin

# Register your models here.
from projects.models import Project, Review, Tag

admin.site.site_header = "Projects"
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
