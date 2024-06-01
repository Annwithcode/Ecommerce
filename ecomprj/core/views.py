from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product,Category,Vendor,CartOrder,CartOrderItems,ProductImages,ProductReview,wishlist,Address

from django.db.models import Count


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

def categery_product_list_view(request,cid):
    category=Category.objects.get(cid=cid)
    products=Product.objects.filter(product_status='published',Category= category)
    context={
        'category':category,
        'products':products,
    }
    return render(request,'core/category-product-list.html',context)


def vendor_list_view(request):
    vendor=Vendor.objects.all()

    context={
        'vendor':vendor
    }
    return render (request,'core/vendor_list.html',context)

