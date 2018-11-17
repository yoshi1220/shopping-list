from django.db import models

class ShopItemPriceHistory(models.Model):
    """お店別単価の履歴"""

    shop = models.CharField(verbose_name='店名', max_length=255)
    item = models.CharField(verbose_name='商品名', max_length=255)
    price = models.PositiveIntegerField(verbose_name='価格', default=0)

    def __str__(self):
        return self.shop + "の" + self.item + "の価格：" + str(self.price) + "円"


class ShoppingList(models.Model):
    """買い物リスト"""
    item = models.CharField(verbose_name='商品名', max_length=255)
    count = models.PositiveIntegerField(verbose_name='数量', default=1)
    shop = models.CharField(verbose_name='店名', max_length=255)
    price = models.PositiveIntegerField(verbose_name='価格', default=0)

    def __str__(self):
        return self.shop + "の" + self.item
