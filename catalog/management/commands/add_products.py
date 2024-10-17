from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(title='птица', description='просто птица')

        products = [
            {'title': 'бедро куринное', 'description': 'Свежее', 'category': category, 'price': '400', 'created_at': '2024-12-12', 'updated_at': '2024-12-10'},
            {'title': 'голени куринные', 'description': 'Свежее', 'category': category, 'price': '300', 'created_at': '2024-10-10', 'updated_at': '2024-12-11'},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.title}'))