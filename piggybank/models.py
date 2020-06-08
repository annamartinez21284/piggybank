from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=64)
  customer_id = models.CharField(max_length=64)
  refresh_token = models.CharField(max_length=64)

  def __str__(self):
      return f"{self.name}, Customer ID: {self.customer_id}"

class Account(models.Model):
  accountholder = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  GBP = 'GBP'
  EUR = 'EUR'
  CURRENCIES = ( (GBP, 'GBP'), (EUR, 'EUR'),)
  currency = models.CharField(max_length=64, choices = CURRENCIES)
  accountUid = models.CharField(max_length=64)

  def __str__(self):
    return f"{self.accountholder.name}, {self.currency}"
