import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

#Жизненный цикл
LIFE_STYLE_CHOICES = ((0, '-'),
                      (1, 'Новинка'),
                      (2, 'Стандарт'),
                      (3, 'Вывод'),
                      (4, 'Под заказ'),
                      (5, 'Акция'))


#Номенклатура
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    article = models.CharField(max_length=100)
    factory = models.ForeignKey('Factory', on_delete=models.PROTECT, related_name="products", blank=True, null=True)
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT, related_name="products", blank=True, null=True)
    life_style = models.IntegerField(choices=LIFE_STYLE_CHOICES, blank=True, null=True)
    props = models.ManyToManyField('Prop', through='PropValue', related_name="products", blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    barcodes = models.JSONField(default=list, blank=True, null=True)

    class Meta:
        ordering = ['article']

    def __str__(self):
        return self.name


#Свойства
class Prop(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


#Значения свойств
class PropValue(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="propvalues")
    prop = models.ForeignKey('Prop', on_delete=models.CASCADE, related_name="propvalues")
    value = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product} - {self.prop} - {self.value}'


#Характеристики
class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_mark = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="batches")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.product} - {self.name}'


#Фото
class Picture(models.Model):

    name = models.CharField(max_length=100, blank=True)
    image = models.URLField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    main = models.BooleanField(default=False)
    deleted_mark = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pictures")
    sort_order = models.PositiveIntegerField(default=99, validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f'{self.product} - {self.image}'


#Страна
class Country(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


#Завод
class Factory(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    image = models.URLField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_mark = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=999, validators=[MinValueValidator(1), MaxValueValidator(999)])

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name


#Коллекция
class Collection(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    image = models.URLField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_mark = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=999, validators=[MinValueValidator(1), MaxValueValidator(999)])
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True)
    life_style = models.IntegerField(choices=LIFE_STYLE_CHOICES, blank=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name

