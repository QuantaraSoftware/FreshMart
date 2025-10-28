from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from .models import Payment
from django.contrib.auth.decorators import login_required
from decimal import Decimal

@login_required
def payment_page(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    if request.method == 'POST':
        method = request.POST.get('payment_method')
        amount = order.total

        payment = Payment.objects.create(
            order=order,
            payment_method=method,
            amount=amount,
            status='pending'
        )

        # If COD, mark order as pending payment
        if method == 'cod':
            order.payment_status = 'pending'
            order.save()
            return redirect('orders:order_confirmation', order_id=order.order_id)

        # If UPI, redirect to Fampay API (example placeholder)
        # TODO: Replace with real Fampay API integration
        if method == 'upi':
            # API call to Fampay
            payment.status = 'completed'
            payment.save()
            order.payment_status = 'completed'
            order.save()
            return redirect('orders:order_confirmation', order_id=order.order_id)

    return render(request, 'payments/payment_page.html', {'order': order})
