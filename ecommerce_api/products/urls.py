from django.urls import path
from . import views

urlpatterns = [
    # Product Endpoints
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),

    # Category Endpoints
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('reviews/', views.ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]

