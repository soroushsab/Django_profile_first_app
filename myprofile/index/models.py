from django.db import models

# Create your models here.

class Content(models.Model):
    ID = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=150)
    Lastname = models.CharField(max_length=150)
    Contactnumber = models.CharField(max_length=11)
    Email = models.URLField()
    LinkedIn = models.URLField()
    GitHub = models.URLField()
    Profile_description = models.TextField()

    def __str__(self):
        return self.Firstname + ' '+ self.Lastname

class Educations(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Level = models.CharField(max_length=255)
    Education_description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    
    def __str__(self):
        return self.Name

class Experience(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)
    Experience_description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    
    def __str__(self):
        return self.Name

class Languages(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name

class Skills(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name

class ContactMe(models.Model):
    ID = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=150)
    Lastname = models.CharField(max_length=150)
    Contactnumber = models.CharField(max_length=11)
    Email = models.URLField()
    description = models.TextField()
    
    def __str__(self):
        return self.Email
