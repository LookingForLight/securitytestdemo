#-*-coding:utf-8-*-
from rest_framework import serializers
from cmdb.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'created', 'name', 'describe', 'price', 'isDelete')
