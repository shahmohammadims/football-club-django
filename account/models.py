from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self , phone_number , first_name , last_name , password=None):
        if not phone_number or not first_name or not last_name:
            raise ValueError('account must have everything (national_code , phone_number , first_name , last_name , sex)')
        user = self.model(
            phone_number = phone_number,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self , phone_number , first_name , last_name , password=None):
        user = self.create_user(
            phone_number = phone_number,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.is_superuser = True
        user.view_profile = False
        user.save()
        return user
        
class Account(AbstractBaseUser , PermissionsMixin):
    phone_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    view_profile = models.BooleanField(default=True)
    objects = AccountManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['-id']
    
    @property
    def debt(self):
        number = 0
        for item in Exercise.objects.filter(accounts=self):
                number += item.category.price
        return number
    
    @property
    def exercises_not_payment(self):
        exer = Exercise.objects.filter(accounts=self)
        
        return exer

class Category(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True)
    date = models.DateField(auto_now_add=True)
    accounts = models.ManyToManyField(Account , blank=True)
    
    def __str__(self):
        return str(self.date)
    
    class Meta:
        ordering = ['-date']