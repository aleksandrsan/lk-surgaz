from rest_framework import serializers

from .models import Client, Contragent, Contract


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'code', 'name']


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'code', 'name', 'isclosed']


class ContragentSerializer(serializers.ModelSerializer):

    contracts = ContractSerializer(many=True)

    class Meta:
        model = Contragent
        fields = ['id', 'code', 'inn', 'kpp', 'name', 'client', 'contracts']
