from django.core.management.base import BaseCommand
from abiverkauf.accounts.models import User
from abiverkauf.store.models import Product

class Command(BaseCommand):
    help = 'Erstellt Demo-Daten (1 Verkäufer, 3 Produkte)'

    def handle(self, *args, **options):
        seller, created = User.objects.get_or_create(username='demo_seller', defaults={'role':'seller', 'email':'seller@example.com'})
        if created:
            seller.set_password('password')
            seller.save()
        Product.objects.get_or_create(seller=seller, name='Schokokuchen', defaults={'price':2.50, 'available':10, 'description': 'Leckerer Schokokuchen'})
        Product.objects.get_or_create(seller=seller, name='Apfelkuchen', defaults={'price':2.00, 'available':8, 'description': 'Frischer Apfelkuchen'})
        Product.objects.get_or_create(seller=seller, name='Kekse', defaults={'price':1.00, 'available':50, 'description': 'Hausgemachte Kekse'})
        self.stdout.write(self.style.SUCCESS('Demo-Daten wurden angelegt - Benutzer: demo_seller / password'))
