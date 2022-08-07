from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from payment.models import Payment
from exercise.models import Exercise

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
        user.is_staff = True
        user.view_profile = False
        user.save()
        return user
        
class Account(AbstractBaseUser , PermissionsMixin):
    phone_number = models.CharField(unique=True , max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = AccountManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return self.phone_number
    
    class Meta:
        ordering = ['-id']
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
    @property
    def debt(self):
        number = 0
        for item in Exercise.objects.filter(accounts=self):
                number += item.category.price
        for item in Payment.objects.filter(account=self):
            number -= item.price
        return number
    
    @property
    def exercises_not_payment(self):
        exer = Exercise.objects.filter(accounts=self)
        for pay in Payment.objects.filter(account=self):
            for item in pay.items.all():
                exer = exer.exclude(id__contains=item.id)
        return exer