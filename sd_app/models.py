from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Transaction(models.Model):
    """
    Transaction model
    """
    # Transaction ID
    transaction_id = models.AutoField(primary_key=True)
    # Amount purchased
    amount = models.FloatField()
    # Location where transaction occurred, true if in state, false if out of state.
    location = models.BooleanField()
    # Date and time of transaction
    date = models.DateTimeField()
    # User who made the transaction
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()