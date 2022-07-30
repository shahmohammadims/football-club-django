from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from payment.models import Payment
from exercise.models import Exercise

class Account(AbstractBaseUser , PermissionsMixin):
    phone_number = models.CharField(unique=True , max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = BaseUserManager()
    
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