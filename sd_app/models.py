from django.db import models
from django.conf import settings

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
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL)