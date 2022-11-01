
from rest_framework import serializers

from .models import Product, PropValue, Picture, ProductPrice, ProductRest, ProductRestDetail

class PropValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropValue
        fields = ['prop', 'id', 'value']


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ['image']


class ProductPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = ['price_zakup', 'price_rozn']


class ProductRestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRest
        fields = ['rest']


class ProductRestDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRestDetail
        fields = ['warehouse', 'date', 'rest']


class ProductSerializer(serializers.ModelSerializer):

    pictures = PictureSerializer(many=True)
    propvalues = PropValueSerializer(read_only=True, many=True)
    prices = ProductPriceSerializer(read_only=True, many=False)
    rests = ProductRestSerializer(many=False)
    restdetails = ProductRestDetailSerializer(many=True)


    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'factory', 'collection', 'life_style', 'barcodes', 'pictures', 'propvalues',
                  'prices', 'rests', 'restdetails']
        extra_kwargs = {
            'created_at': {'read_only': True}
        }


