from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from django_filters.views import FilterView

from .models import ShoppingList
from .filters import ShoppingListFilter

class IndexView(PaginationMixin, FilterView):
    """買い物リストの一覧"""

    # FilterView
    template_name = 'shopping_list/index.html'
    context_object_name = 'shopping_list'
    model = ShoppingList
    queryset = ShoppingList.objects.all().order_by('item')

    # django_filters
    filterset_class = ShoppingListFilter
    strict = False

    # pure_pagination
    object = ShoppingList

    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)
