from django_filters import FilterSet
from django_filters import filters

from .models import ShoppingList

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class ShoppingListFilter(FilterSet):

    item = filters.CharFilter(label='商品', lookup_expr='contains')
    shop = filters.CharFilter(label='お店', lookup_expr='contains')

    order_by = MyOrderingFilter(
        fields=(
            ('item', 'item'),
            ('shop', 'shop'),
        ),
        field_labels={
            'item': '商品',
            'shop': 'お店',
        },
        label='並び順'
    )

    class Meta:
        model = ShoppingList
        fields = ('item', 'shop', 'price',)
