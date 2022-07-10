from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Transaction(models.Model):
    """
    Transaction model
    """        
    # Amount being purchased
    amount = models.FloatField()
    # Location where transaction occurred, true if in state, false if out of state.
    location = models.CharField(max_length=100)    
    # Date and time of desired delivery
    delivery_date = models.CharField(max_length=15)
    # User who made the transaction
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Amount: " + str(self.amount) + " gal. Location: at " + str(self.location) + ". Delivery Date: " + str(self.delivery_date)

STATE_CHOICES = (
    ('al','AL'),
    ('ak','AK'),
    ('az','AZ'),
    ('ar','AR'),
    ('ca','CA'),
    ('co','CO'),
    ('ct','CT'),
    ('de','DE'),
    ('fl','FL'),
    ('ga','GA'),
    ('hi','HI'),
    ('id','ID'),
    ('il','IL'),
    ('in','IN'),
    ('ia','IA'),
    ('ks','KS'),
    ('ky','KY'),
    ('la','LA'),
    ('me','ME'),
    ('md','MD'),
    ('ma','MA'),
    ('mi','MI'),
    ('mn','MN'),
    ('ms','MS'),
    ('mo','MO'),
    ('mt','MT'),
    ('ne','NE'),
    ('nv','NV'),
    ('nh','NH'),
    ('nj','NJ'),
    ('nm','NM'),
    ('ny','NY'),
    ('nc','NC'),
    ('nd','ND'),
    ('oh','OH'),
    ('ok','OK'),
    ('or','OR'),
    ('pa','PA'),
    ('ri','RI'),
    ('sc','SC'),
    ('sd','SD'),
    ('tn','TN'),
    ('tx','TX'),
    ('ut','UT'),
    ('vt','VT'),
    ('va','VA'),
    ('wa','WA'),
    ('wv','WV'),
    ('wi','WI'),
    ('wy','WY'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True)
    zip_code = models.CharField(max_length=9, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()