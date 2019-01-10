from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=20, unique=True)
    leader = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    access = models.IntegerField(default='0')
    name = models.CharField(max_length=10, null=True)


class Project(models.Model):
    department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    leader = models.ForeignKey(User, related_name='leader', on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    content = models.CharField(max_length=500, default='')
    begin_time = models.DateField(null=False, default=timezone.now)
    end_time = models.DateField(null=False, default=timezone.now)
    personnel = models.ManyToManyField(User, related_name='personnel')

    def __str__(self):
        return self.title


class Expend(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=30, default='')
    number = models.CharField(max_length=15, blank=False)
    agreement = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title


class ConfirmExpend(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Expend, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, blank=False)
    agreement = models.CharField(max_length=500, default='')


class Receivable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=30, default='')
    number = models.CharField(max_length=15, blank=False)
    agreement = models.CharField(max_length=500, default='')


class Advance(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    receivable = models.ForeignKey(Receivable, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, blank=False, default='0')
    agreement = models.CharField(max_length=500, default='')


class Income(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Receivable, on_delete=models.CASCADE)
    confirm_num = models.CharField(max_length=15, blank=False, default='0')
    tax_rate = models.CharField(max_length=10, blank=False)
    invoice_document = models.CharField(max_length=500, default='')
