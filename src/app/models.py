from django.db import models

# Create your models here.

User = ("User")

# ● Category: name, slug, icon (image).
# ● Product: category (FK), name, description, price, stock_count, created_at.
# ● Order: user (FK), total_price, status (new, paid, delivered, cancelled), created_at.
# ● OrderItem: order (FK), product (FK), quantity, price_at_purchase

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    price = models.CharField(default=0)
    stock_count = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):

    STATUS = (
        ('new', 'new'),
        ('paid', 'paid'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled'),
    )
        

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    
# ● OrderItem: order (FK), product (FK), quantity, price_at_purchase


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(default=0)
    price_at_purchase = models.IntegerField(default=0)

    def __str__(self):
        return self.product

