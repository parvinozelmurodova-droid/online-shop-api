from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

class ProductListAPIView(generics.ListAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer


class CategoryListAPIView(generics.ListAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer