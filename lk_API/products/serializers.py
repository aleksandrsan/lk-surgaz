
from rest_framework import serializers

from .models import Product, PropValue, Picture

class PropValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropValue
        fields = ['prop', 'id', 'value']


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):

    pictures = PictureSerializer(many=True)
    propvalues = PropValueSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'factory', 'collection', 'life_style', 'barcodes', 'pictures', 'propvalues']
        extra_kwargs = {
            'created_at': {'read_only': True}
        }


