from django.contrib import admin


from .models import Product, Factory, Collection, Batch, PropValue, Picture, Prop, Country

class BatchInlineAdmin(admin.StackedInline):
    model = Batch
    extra = 0

class PictureInlineAdmin(admin.StackedInline):
    model = Picture
    extra = 0

class PropValueInlineAdmin(admin.StackedInline):
    model = PropValue
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [BatchInlineAdmin, PictureInlineAdmin, PropValueInlineAdmin]
    pass

@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Prop)
class PropAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass