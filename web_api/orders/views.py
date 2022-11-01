


#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
#from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from contragents.models import Contragent

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id']

    def get_queryset(self):
        contragent_array = Contragent.objects.filter(client=self.request.user.client)
        return Order.objects.filter(contragent__in=contragent_array)
