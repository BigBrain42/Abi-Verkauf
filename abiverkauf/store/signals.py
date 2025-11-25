from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Notification, OrderItem
from django.core.mail import send_mail

@receiver(post_save, sender=OrderItem)
def order_item_created(sender, instance, created, **kwargs):
    if created:
        order = instance.order
        seller = instance.product.seller
        Notification.objects.create(
            user=seller,
            message=f'Neue Bestellung #{order.id} - {instance.quantity}x {instance.product.name}.'
        )
        # Send email to seller
        if seller.email:
            send_mail(
                f'Neue Bestellung #{order.id}',
                f'Produkt: {instance.product.name}\nMenge: {instance.quantity}\nBestellnummer: {order.id}',
                'noreply@example.com',
                [seller.email],
                fail_silently=True,
            )
        # Notify customer by email
        if order.customer and order.customer.email:
            send_mail(
                f'Bestellbestätigung #{order.id}',
                f'Deine Bestellung für {instance.product.name} wurde aufgenommen. Bestellnummer: {order.id}',
                'noreply@example.com',
                [order.customer.email],
                fail_silently=True,
            )
