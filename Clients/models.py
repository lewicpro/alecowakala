from django.db import models
from django.contrib.auth.models import User
import random, string
from django.template.defaultfilters import truncatechars

# Create your models here.
class Clients(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    fullname=models.CharField(max_length=120, blank=True, null=True)
    email=models.CharField(max_length=120, blank=True, null=True)
    privillages=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(unique=True, max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    commission=models.CharField(max_length=120, blank=True, null=True)
    Nationality=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Client Lists"

class CashOut(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    payment=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    commission=models.CharField(max_length=120, blank=True, null=True)
    salio=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Cash Out"

class CashIn(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    payment=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    commission=models.CharField(max_length=120, blank=True, null=True)
    salio=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Cash In"

class Voucher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    payment=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    commission=models.CharField(max_length=120, blank=True, null=True)
    salio=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Voucher"


    
class InOffice(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Expenses in office"

class OutOffice(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Expenses Out office"

class CheckPayment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Check payment"

class PendingIn(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Pending In"


class PendingOut(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    service=models.CharField(max_length=120, blank=True, null=True)
    transactionid=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Pending Out"


class Processors(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    service_name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Processors Lists"

class Capital(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    service_name=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    commission=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Capital remaining"

class Balance(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, max_length=120, blank=True, null=True)
    date=models.CharField(max_length=120, blank=True, null=True)
    processor=models.CharField(max_length=120, blank=True, null=True)
    amount=models.CharField(max_length=120, blank=True, null=True)
    commission=models.CharField(max_length=120, blank=True, null=True)
    company=models.CharField(max_length=120, blank=True, null=True)
    officer=models.CharField(max_length=120, blank=True, null=True)
    description=models.CharField(max_length=120, blank=True, null=True)
    status=models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Capital remaining"


    