from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, contacts, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='blog_post'),

]
