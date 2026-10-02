from django.contrib import admin
from .models import StudentProfile, CompanyProfile, Job,Application
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(CompanyProfile)
admin.site.register(Job)
admin.site.register(Application)
