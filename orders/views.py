from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from products.models import Product
from accounts.models import Address
from django.contrib.auth.decorators import login_required
from decimal import Decimal

@login_required
def checkout(request):
    cart = Cart(request)
    addresses = request.user.addresses.all()
    if request.method == 'POST':
        address_id = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        address = get_object_or_404(Address, id=address_id)
        
        subtotal = cart.get_total_price()
        delivery_charge = Decimal('20.00')  # example
        total = subtotal + delivery_charge

        order = Order.objects.create(
            user=request.user,
            delivery_address=address,
            delivery_name=address.name,
            delivery_phone=address.phone,
            delivery_address_line=f"{address.address_line1}, {address.address_line2}, {address.city}, {address.state}, {address.pincode}",
            subtotal=subtotal,
            delivery_charge=delivery_charge,
            discount=Decimal('0.00'),
            total=total,
            payment_method=payment_method,
            payment_status='pending'
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                product_name=item['product'].name,
                product_price=item['price'],
                quantity=item['quantity'],
                subtotal=item['total_price']
            )
        cart.clear()
        return redirect('orders:order_confirmation', order_id=order.order_id)

    return render(request, 'orders/checkout.html', {'cart': cart, 'addresses': addresses})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})

@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order_list.html', {'orders': orders})
