from django.contrib import admin

from .models import ShoppingList, ShopItemPriceHistory

admin.site.register(ShopItemPriceHistory)
admin.site.register(ShoppingList)