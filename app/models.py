from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " id: " +str(self.id)
    

class Profile(models.Model):
    sex_choice = (
        ("male","male"),
        ("female","female")
    )

    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    sex = models.CharField(max_length=10, choices=sex_choice, default="male")

    def __str__(self):
        return self.name



