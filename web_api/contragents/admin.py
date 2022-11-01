from django.contrib import admin

from .models import Contragent, Contract, Client


class ContractInlineAdmin(admin.StackedInline):
    model = Contract
    extra = 0


@admin.register(Contragent)
class ContragentAdmin(admin.ModelAdmin):
    inlines = [ContractInlineAdmin]
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
