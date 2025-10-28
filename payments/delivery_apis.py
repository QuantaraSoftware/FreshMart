import requests
from django.conf import settings

BORZO_BASE_URL = settings.BORZO_BASE_URL
BORZO_API_KEY = settings.BORZO_API_KEY
BORZO_API_SECRET = settings.BORZO_API_SECRET

def create_borzo_order(order):
    """Create order with Borzo delivery API"""
    data = {
        "customer_name": order.delivery_name,
        "customer_phone": order.delivery_phone,
        "pickup_address": "Your Store Address",
        "delivery_address": order.delivery_address_line,
        "items": [{"name": item.product_name, "quantity": item.quantity} for item in order.items.all()],
        "cod_amount": float(order.total),
    }
    headers = {
        "API-KEY": BORZO_API_KEY,
        "API-SECRET": BORZO_API_SECRET,
    }
    response = requests.post(f"{BORZO_BASE_URL}/orders/create", json=data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        order.delivery_partner = "Borzo"
        order.tracking_id = result.get("tracking_id")
        order.tracking_url = result.get("tracking_url")
        order.save()
        return result
    return None
