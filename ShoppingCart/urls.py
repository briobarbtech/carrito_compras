from django.urls import path
from .views import ProductUpdateView,ProductDeleteView, ProductListView, ProductCreateView, ProductDetailView

app_name='store'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/',ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(),name='product_delete')
    ]