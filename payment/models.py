from django.db import models

class Payment(models.Model):
    account = models.ForeignKey("account.Account", on_delete=models.SET_NULL , null=True)
    price = models.IntegerField()
    items = models.ManyToManyField('account.Exercise')
    
    def __str__(self):
        return self.account