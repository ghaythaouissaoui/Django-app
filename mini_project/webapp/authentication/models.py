from django.db import models

class users(models.Model):
    username= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)

    def __str__(self):
        return self.name

