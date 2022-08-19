
import json

from django.core.management.base import BaseCommand

from products.serializers import ProductSerializer


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('products.json', 'r') as f:
            data = json.load(f)

        serializer = ProductSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print('MISTAKE')



