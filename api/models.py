from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):

    title = models.CharField(max_length=200)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    expense_categories = (
        ("Housing", "Housing"),
        ("Transportation", "Transportation"),
        ("Food", "Food"),
        ("Health", "Health"),
        ("Entertainment", "Entertainment"),
        ("DebtPayments", "Debt Payments"),
        ("PersonalCare", "Personal Care"),
        ("Education", "Education"),
        ("Savings", "Savings"),
        ("Miscellaneous", "Miscellaneous")
    )

    category=models.CharField(max_length=200,choices=expense_categories,default="Miscellaneous")

    priority_options=(
        ("Need","Need"),
        ("Want","Want")
    )

    priority=models.CharField(max_length=100,choices=priority_options,default="Need")

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):

        return self.title
    
    
class Income(models.Model):

    title=models.CharField(max_length=200)

    amount=models.PositiveIntegerField()

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    income_categories = (
        ("Salary", "Salary"),
        ("Business", "Business"),
        ("Investment", "Investment"),
        ("Rental", "Rental"),
        ("Interest", "Interest"),
        ("Dividend", "Dividend"),
        ("Royalty", "Royalty"),
        ("Capital", "Capital"),
        ("Pension", "Pension"),
        ("SocialSecurity", "SocialSecurity")
    )

    category=models.CharField(choices=income_categories,max_length=200,default="Salary")

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):
        
        return self.title