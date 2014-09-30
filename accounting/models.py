from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    name = models.CharField(max_length=10)

class Account(models.Model):
    user = models.ForeignKey(User)
    currency = models.ForeignKey(Currency)
    amount=models.IntegerField()

    def withdraw(self, amount, target):
        assert self.amount >= amount
        assert self.currency.name == target.currency.name
        self.amount -= amount
        target.amount +=amount