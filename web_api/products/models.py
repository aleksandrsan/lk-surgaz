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
    name = models.CharField(max_length=250, verbose_name='Название')
    article = models.CharField(max_length=100, verbose_name='Артикул')
    factory = models.ForeignKey('Factory', on_delete=models.PROTECT, related_name="products",
                                blank=True, null=True, verbose_name='Завод')
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT, related_name="products",
                                   blank=True, null=True, verbose_name='Коллекция')
    life_style = models.IntegerField(choices=LIFE_STYLE_CHOICES, blank=True, null=True, verbose_name='Жизненный цикл')
    props = models.ManyToManyField('Prop', through='PropValue', related_name="products", blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    barcodes = models.JSONField(default=list, blank=True, null=True, verbose_name='Штрихкоды')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['article']

    def __str__(self):
        return self.name


#Свойства
class Prop(models.Model):

    name = models.CharField(max_length=250, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
        ordering = ['name']

    def __str__(self):
        return self.name


#Значения свойств
class PropValue(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="propvalues",
                                verbose_name='Товар')
    prop = models.ForeignKey('Prop', on_delete=models.CASCADE, related_name="propvalues", verbose_name='Свойства')
    value = models.CharField(max_length=100, verbose_name='Значение')

    class Meta:
        verbose_name = 'Значение свойства'
        verbose_name_plural = 'Значения свойств'
        ordering = ['product']

    def __str__(self):
        return f'{self.product} - {self.prop} - {self.value}'


#Характеристики
class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, verbose_name='Наименование')
    updated_at = models.DateTimeField(auto_now=True)
    deleted_mark = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="batches", verbose_name='Товар')

    class Meta:
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'
        ordering = ['name']

    def __str__(self):
        return f'{self.product} - {self.name}'


#Фото
class Picture(models.Model):

    name = models.CharField(max_length=100, blank=True)
    image = models.URLField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    main = models.BooleanField(default=False, verbose_name='Главная')
    deleted_mark = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pictures", verbose_name='Товар')
    sort_order = models.PositiveIntegerField(default=99, validators=[MinValueValidator(1), MaxValueValidator(99)],
                                             verbose_name='Порядок сортировки')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['sort_order']

    def __str__(self):
        return f'{self.product} - {self.image}'


#Страна
class Country(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Наименование')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']

    def __str__(self):
        return self.name


#Завод
class Factory(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Наименование')
    image = models.URLField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_mark = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=999, validators=[MinValueValidator(1), MaxValueValidator(999)])

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'
        ordering = ['sort_order']

    def __str__(self):
        return self.name


#Коллекция
class Collection(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Наименование')
    image = models.URLField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_mark = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=999, validators=[MinValueValidator(1), MaxValueValidator(999)])
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, verbose_name='Страна')
    life_style = models.IntegerField(choices=LIFE_STYLE_CHOICES, blank=True, verbose_name='Жизненный цикл')

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        ordering = ['sort_order']

    def __str__(self):
        return self.name

#Цены
class ProductPrice(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="prices", verbose_name='Товар')
    price_zakup = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Продажи1')
    price_rozn = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='РРЦ')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return f'{self.product} - {self.price_zakup} - {self.price_rozn}'


#Остатки
class ProductRest(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="rests", verbose_name='Товар')
    rest = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Остаток (общий)')

    class Meta:
        verbose_name = 'Остатки'
        verbose_name_plural = 'Остатки'

    def __str__(self):
        return f'{self.product} - {self.rest}'


#Остатки
class ProductRestDetail(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="restdetails", verbose_name='Товар')
    warehouse = models.CharField(max_length=100, blank=True, verbose_name='Склад')
    date = models.DateField(blank=True, null=True, verbose_name='Товар')
    rest = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Остаток')

    class Meta:
        verbose_name = 'Детальные остатки'
        verbose_name_plural = 'Детальные остатки'

    def __str__(self):
        return f'{self.product} - {self.rest}'

