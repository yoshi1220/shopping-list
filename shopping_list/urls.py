from django.urls import path

from . import views

app_name = 'shopping_list'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
