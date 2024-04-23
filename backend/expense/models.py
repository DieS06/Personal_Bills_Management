from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    app_label = 'category'
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class Expense(models.Model):
    app_label = 'expense'
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255) 
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.date} - {self.amount} - {self.description[:20]}" 