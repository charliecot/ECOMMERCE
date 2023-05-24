from django.urls import path
from .import views

app_name= 'ECOM'

urlpatterns = [
    path('', views.all_products, name='all_product'),
    path('item/<slug:slug>/', views.product_detail, name='product'),
    path('search/<slug:cat_slug>/', views.category_detail, name='category'),
]