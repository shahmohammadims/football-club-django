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
        user.save()
        return user
        
class Account(AbstractBaseUser , PermissionsMixin):
    phone_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['-id']