from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField



STATUS_CHOICE=(
    ('process','Processing'),
    ('shipped','Shipped'),
    ('delivered','Delivered')
)

STATUS=(
    ('draft','Draft'),
    ('disabled','Disabled'),
    ('rejected','Rejected'),
    ('in review','In Review'),
    ('published','Published')
)

RATING=(
    (1,'★☆☆☆☆'),
    (2,'★★☆☆☆'),
    (3,'★★★☆☆'),
    (4,'★★★★☆'),
    (5,'★★★★★')


)


from userauths.models import User

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)




class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=20,prefix='cat',alphabet='abcde12345')
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Categories')


    class Meta:
        verbose_name_plural="Categories"

    def categoty_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def __str__(self):
        return self.title
    
class Vendor(models.Model):
    vid=ShortUUIDField(unique=True,length=7,max_length=10,prefix='VEN',alphabet='abcde12345')
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='user_directory_path')
    description=models.TextField(null=True,blank=True)

    address=models.CharField(max_length=100,default='Kozhikode')
    contact=models.CharField(max_length=100,default='Kozhikode')
    chat_resp_time=models.CharField(max_length=100,default='100')
    
    shipping_on_time=models.CharField(max_length=100,default='100')
    authentic_rating=models.CharField(max_length=100,default='100')
    days_return=models.CharField(max_length=100,default='100')
    warranty_period=models.CharField(max_length=100,default='100')



    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural="vendor"

    def vender_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    pid=ShortUUIDField(unique=True,length=10,max_length=20,prefix='cat',alphabet='abcde12345')
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='Category')


    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='user_directory_path',default='product.jpg')
    description=models.TextField(null=True,blank=True,default='This is a product')

    price=models.DecimalField(max_digits=10,decimal_places=2,default='2.99')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='2.99')
    specification=models.TextField(null=True,blank=True)
    # tags=models.ForeignKey(tagsgs)
    product_status=models.CharField(choices=STATUS,max_length=10,default='in_review')

    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)
    featured=models.BooleanField(default=True)
    digital=models.BooleanField(default=True)
    pid=ShortUUIDField(unique=True,length=4,max_length=10,prefix='sku',alphabet='1234567890')

    date=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(null=True,blank=True)


    class Meta:
        verbose_name_plural="Product"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price=self.price/self.old_price*100
        return new_price
    
class ProductImages(models.Model):
    images=models.ImageField(upload_to='product-images',default='product.jpg')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="ProductImages"


# class CartOrder(models.Model):
    
#     user=models.ForeignKey(User,on_delete=models.CASCADE)

#     price=models.DecimalField(max_digits=10,decimal_places=2,default='2.99')

#     paid_status=models.BooleanField(default=False)

#     order_date=models.DateTimeField(auto_now_add=True)

#     product_status=models.CharField(choices=STATUS_CHOICE,max_length=30,default='processing')

#     class Meta:
#         verbose_name_plural="Cart Order"
        


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=2.99)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField()
    product_status = models.CharField(choices=STATUS_CHOICE,max_length=30,default='processing')

    class Meta:
        verbose_name_plural = "Cart Orders"



class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_number=models.CharField(max_length=200)
    product_status=models.CharField(max_length=200)
    item=models.CharField(max_length=200)

    image=models.CharField(max_length=200)
    qty=models.IntegerField(default=0)    
    price=models.DecimalField(max_digits=10,decimal_places=2,default='2.99')
    total=models.DecimalField(max_digits=10,decimal_places=2,default='2.99')


    class Meta:
        verbose_name_plural="Cart Order Items"

    def order_image(self):
        return mark_safe('<img src="/media/"%s" width="50" height="50" />' %(self.image))

class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    review=models.TextField()
    rating=models.IntegerField(choices=RATING,default=None)
    date=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural="Product Reviews"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="wishlist"

    def __str__(self):
        return self.product.title

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=100,null=True)
    status=models.BooleanField(default=False)
class Meta:
        verbose_name_plural="Address"

