from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Area(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Client(models.Model):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(blank=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    dob = models.DateField(null=True, blank=True)
    mail_id = models.EmailField(blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    ACCOUNT_CHOICES = [
        ('saving', 'Saving Account'),
        ('current', 'Current Account'),
        ('business', 'Business Account'),
        ('student', 'Student Account'),
    ]
    account = models.CharField(max_length=255, choices=ACCOUNT_CHOICES)
    materials = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name
