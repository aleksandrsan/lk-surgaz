from django.db import models

import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from contragents.models import Contragent, Contract
from products.models import Product, Batch

#Статусы заказов
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, default='', blank=True)
    color = models.CharField(max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


#Товары заказов
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)            # Номенклатура
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)    # Партия
    quantity = models.IntegerField(default=0, blank=True)                                   # Количество
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)     # Цена
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)       # НДС
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)       # Сумма
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, related_name='items', related_query_name='items',
                              blank=True, null=True)                                        # Заказ
    itemnumber = models.SmallIntegerField()                                                 # Номер строки

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        ordering = ['itemnumber']

    def __str__(self):
        return 'OrderItem:'


#Заказы
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #slug = models.SlugField(unique=True, null=True, blank=True)
    number = models.CharField(max_length=9)
    date = models.DateTimeField(null=True)
    contragent = models.ForeignKey(Contragent, on_delete=models.PROTECT, related_name="orders", blank=False, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, related_name="orders", blank=False, null=True)
    status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, blank=True, null=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)       # Сумма

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['number']


    #def get_queryset(self):
    #    user = self.request.user

       # return Order.objects.filter(number=user)


    def __str__(self):
        return str(self.number)

