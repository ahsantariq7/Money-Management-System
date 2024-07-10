# models.py

# Import necessary modules if not already imported
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username  # Display the username of the associated user


class Account(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.CharField(max_length=100)  # Username for the account
    password = models.CharField(max_length=255)  # Encrypted password
    website = models.URLField(
        blank=True, null=True
    )  # Website associated with the account

    def __str__(self):
        return f"{self.name} ({self.user_profile.user.username})"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ExpensePurpose(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    purpose = models.ForeignKey(ExpensePurpose, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.amount} - {self.description}"


class Budget(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"


class Reminder(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title


class FinancialGoal(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OtherAccount(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.account_number} - {self.institution}"


class Loan(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lender_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.lender_name} - {self.amount}"


class LoanGiven(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.borrower_name} - {self.amount}"


class Enjoyment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.activity


class EmailPassword(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


models_name = [
    UserProfile,
    Account,
    Category,
    ExpensePurpose,
    Transaction,
    Budget,
    Reminder,
    FinancialGoal,
    OtherAccount,
    Loan,
    LoanGiven,
    Enjoyment,
    EmailPassword,
]
