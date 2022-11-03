from .models import ProductInBasket


def getting_basket_info(request):
    if request.user.is_authenticated:
        session_key = request.user.email
    else:
        session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products.count()
    products_basket_list = products.values_list('size', flat=True)
    return locals()
