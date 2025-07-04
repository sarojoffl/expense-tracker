from django.db import models
from django.contrib.auth.models import User


class ExpenseIncome(models.Model):
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    TAX_TYPES = [
        ('flat', 'Flat'),
        ('percentage', 'Percentage'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='expenses'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_type = models.CharField(max_length=10, choices=TAX_TYPES, default='flat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        if self.tax_type == 'flat':
            return self.amount + self.tax
        return self.amount + (self.amount * self.tax / 100)

    def __str__(self):
        return f"{self.title} ({self.transaction_type}) - {self.total}"

    class Meta:
        ordering = ['-created_at']
