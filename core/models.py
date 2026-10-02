from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    education = models.CharField(max_length=100)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company_name


class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    skills_required = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_date = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,  default='Pending')

    def __str__(self):
            return self.student.user.username
    









