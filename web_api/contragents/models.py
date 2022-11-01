
import uuid

from django.db import models

#Контрагенты
class Contragent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=9)
    inn = models.CharField(max_length=20, default='', blank=True)
    kpp = models.CharField(max_length=20, default='', blank=True)
    name = models.CharField(max_length=250, default='', blank=True)
    client = models.ForeignKey('client', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ['name']

    def __str__(self):
        return self.name


#Договоры
class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=9)
    name = models.CharField(max_length=200, null=True, blank=True)
    contragent = models.ForeignKey('Contragent', on_delete=models.SET_NULL, null=True)
    isclosed = models.BooleanField()

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
        ordering = ['name']

    def __str__(self):
        return self.name


#Клиенты
class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=9)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']

    def __str__(self):
        return self.name
