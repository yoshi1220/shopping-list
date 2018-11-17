from django.shortcuts import render
from django.views import View

from .models import ShoppingList

class IndexView(View):
    def get(self, request, *args, **kwargs):
        queryset = ShoppingList.objects.all()

        context = {
            'shopping_list': queryset
        }

        return render(request, 'shopping_list/index.html', context)
