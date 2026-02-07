from django.db import models
from django.utils import timezone

#Define the validator

validate_at_symbol=RegexValidator(
    regex='@',
    message='Field must contain the @ symbol',
    code='invalid_at_symbol'
)
class Customer(models.Model):
    customer_name=models.CharField(50)
    customer_id=models.IntegerField()
    email_address=models.CharField(max_length=50,validators=[validate_at_symbol] )
    Order_time=models.TimeField()

class Chef(models.Model):
    chef_name=models.CharField(50)
    chef_id=models.IntegerField()



