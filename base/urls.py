from django.urls import path
from .views import ProductListAPIView,ProductCreateAPIView,ProductRetrieveUpdateDestroyAPIView,CategoryListAPIView

urlpatterns = [
    path("GET/products/", ProductListAPIView.as_view()),
    path("PUT/products/", ProductCreateAPIView.as_view()),
    path("DELETE/products/<int:pk>", ProductRetrieveUpdateDestroyAPIView.as_view()),
    path("GET/categories/", CategoryListAPIView.as_view())
]
