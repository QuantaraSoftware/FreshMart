from django.db import models

class Payment(models.Model):
    """Payment records"""
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')

    # UPI specific
    upi_transaction_id = models.CharField(max_length=100, blank=True)
    upi_reference_number = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for {self.order.order_id}"
