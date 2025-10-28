from .cart import Cart

def cart_count(request):
    """Make cart count available in all templates"""
    cart = Cart(request)
    return {'cart_count': len(cart)}
