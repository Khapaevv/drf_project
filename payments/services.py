import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def create_stripe_product(product):
    """ Создает продукт в Stripe и возвращает его ID """
    stripe_product = stripe.Product.create(name=product.name)
    return stripe_product.id

def create_stripe_price(payment_amount, product_id):
    """ Создает цену в Stripe, используя ID продукта """
    return stripe.Price.create(
        unit_amount=payment_amount * 100,
        currency="rub",
        product=product_id,
    )

def create_stripe_session(price):
    """Создает сессию на оплату с страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")