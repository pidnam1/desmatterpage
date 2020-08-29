from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    is_company = models.BooleanField(default=False)
    is_manufacturer = models.BooleanField(default=False)




    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return self.user.username

class Product(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    description = models.CharField(max_length=100, blank = True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantityAvailable = models.IntegerField()
    availability = models.BooleanField()







