from django.urls import path
from .views import ProductDetailView, ProductupdateView, ProductCreateView, ProductdeleteView

urlpatterns = [
    path('<int:pk>/product_detail/', ProductDetailView.as_view(), name='product-detail' ),
    path('<int:pk>/product_update/', ProductupdateView.as_view(), name='product-update' ),
    path('product_create/', ProductCreateView.as_view(),
         name='product-create'),
    path('<int:pk>/product_delete/', ProductdeleteView.as_view(),
         name='product-delete'),
]