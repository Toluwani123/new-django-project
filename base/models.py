from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
BANK_CHOICES =(
    ("Kuda","Kuda Bank"),
    ("Zenith","Zenith Bank"),
    ("Guarantee Trust","Guarantee Trust Bank"),
    ("First","First Bank"),
    ("Stanbic IBTC","Stanbic IBTC Bank"),
    ("Sterling","Sterling Bank")
)
class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bank_name = models.CharField(choices=BANK_CHOICES, max_length=50)
    account_number = models.IntegerField(blank = False, null = False, validators=[ MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bank_name
        
    class Meta: 
        ordering = ['bank_name'] 