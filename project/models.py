from _ast import mod

from django.db import models
from userProfile import models as UserModel
from django.utils import timezone


# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.category


class Project(models.Model):
    user = models.ForeignKey(UserModel.UserProfile, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, default='Project Title')
    start_date = models.DateField(default=timezone.now, null=True)
    end_date = models.DateField(default=timezone.now, null=True)
    total_rating = models.IntegerField(default=0, null=True)
    total_target = models.BigIntegerField(default=0, null=True)

    def __str__(self):
        return self.title


class ProjectPics(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    project_picture = models.ImageField(upload_to='images/', null=True, default='images/noimage.jpg')


class ProjectTags(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    project_tag = models.CharField(max_length=50, null=True)


class ProjectReports(models.Model):
    user = models.ForeignKey(UserModel.UserProfile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    report = models.TextField(max_length=250, null=True)


class ProjectRatings(models.Model):
    user = models.ForeignKey(UserModel.UserProfile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user_rating = models.IntegerField(default='0', null=True)


class ProjectComments(models.Model):
    user = models.ForeignKey(UserModel.UserProfile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    comment_body = models.TextField(max_length=250, null=True)
    comment_reports = models.IntegerField(default=0, null=True)


class ProjectDonations(models.Model):
    user = models.ForeignKey(UserModel.UserProfile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    donation_amount = models.BigIntegerField(default=0, null=True)
