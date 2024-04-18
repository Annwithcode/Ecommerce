from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product,Category,Vendor,CartOrder,CartOrderItems,ProductImages,ProductReview,wishlist,Address




# Create your views here.
def index(request):
    products=Product.objects.filter(product_status='published')
    context={
        "products":products
    }
    return render(request,'core/index.html',context)

def categorylist_view(request):
    categories=Category.objects.all()

    context={
        'categories':categories
    }

    return render(request,'core/category_list.html',context)