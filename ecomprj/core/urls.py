from django.urls import path

from core.views import *

urlpatterns = [
#  HOMEPAGE
    path('',index,name='index'),

    # PRODUCT
    path('category/',categorylist_view,name='category'),
    path('category/<cid>/',categery_product_list_view,name='category-product-list'),

    # VENDER

    path('vendor/',vendor_list_view,name='vendor_list')
    
]
