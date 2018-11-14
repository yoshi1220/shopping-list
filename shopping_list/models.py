from django.db import models

class Item(models.Model):
    """商品"""

    name = models.CharField(verbose_name='商品名', max_length=255)

    def __str__(self):
        return self.name

class Shop(models.Model):
    """お店"""

    name = models.CharField(verbose_name='店名', max_length=255)
    price = models.PositiveIntegerField(verbose_name='価格', default=0)

    def __str__(self):
        return self.name

class ShopItemPrice(models.Model):
    """お店別単価"""

    shop = models.ForeignKey(Item, verbose_name='お店', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name='商品', on_delete=models.CASCADE)

class ShoppingList(models.Model):
    """買い物リスト"""

    purchase_item = models.ForeignKey(Item, verbose_name='買う物', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='数量', default=1)
    shop = models.ForeignKey(Shop, verbose_name='お店', on_delete=models.CASCADE)
    price = models.ForeignKey(ShopItemPrice, verbose_name='お店の値段', on_delete=models.CASCADE)
