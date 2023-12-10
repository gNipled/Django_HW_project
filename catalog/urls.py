from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, contacts, ProductDetailView


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
]
