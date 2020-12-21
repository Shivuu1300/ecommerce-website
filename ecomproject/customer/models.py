from django.db import models
from phone_field import PhoneField



class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique = True)
    phone = PhoneField(blank=True)
    profile_image = models.ImageField(upload_to = 'images/')
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

