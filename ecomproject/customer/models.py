from django.db import models
from phone_field import PhoneField


def upload_image(instance,filename):
    return 'images/{}/{}'.format(instance.username,filename)
class Customer(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique = True)
    phone = PhoneField(blank=True)
    profile_image = models.ImageField(upload_to = upload_image, default='images/dashboard-default-avatar2.png')
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name + ' ' + str(self.phone)
    

