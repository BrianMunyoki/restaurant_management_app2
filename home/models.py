from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator


class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    email_address=models.EmailField(max_length=50)
    Order_time=models.TimeField()
    
    def __str__(self):
        return f"{self.customer_name} - {self.email_address}"

class Chef(models.Model):
    chef_name=models.CharField(max_length=50)
    def __str__(self):
        return self.chef_name
class Food(models.Model):
    food_name=models.CharField(max_length=50)
    Ingredients=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.food_name} - {self.Ingredients}"
class Menu(models.Model):
    table_number=models.IntegerField()
    food=models.ForeignKey(Food ,on_delete=models.CASCADE)
    chef=models.ForeignKey(Chef ,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.table_number} -{self.food} -{self.chef} - {self.customer}"