from rest_framework.serializers import ModelSerializer
from .models import Category,Product,Order,OrderItem


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'