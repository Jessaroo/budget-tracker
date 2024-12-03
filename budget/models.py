from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)  # Automatically add the current date

    def __str__(self):
        return f"{self.category} - {self.description}"