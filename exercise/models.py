from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True)
    date = models.DateField(auto_now_add=True)
    accounts = models.ManyToManyField('account.Account' , blank=True)
    
    def __str__(self):
        return str(self.date)
    
    class Meta:
        ordering = ['-date']