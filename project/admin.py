from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Project)
admin.site.register(ProjectRatings)
admin.site.register(ProjectPics)
admin.site.register(ProjectReports)
admin.site.register(ProjectDonations)
admin.site.register(Categories)
admin.site.register(ProjectComments)




