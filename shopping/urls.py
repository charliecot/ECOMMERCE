from django.urls import path
from . import views

app_name ='shopping'

urlpatterns = [
    path('',views.all_shopping_items, name='all_items' ),
    path('add/',views.add_items, name='add_items' ),
    path('delete/',views.delete_items, name='delete_items' ),
    path('update/',views.update_items, name='update_items' ),
    
    
]
