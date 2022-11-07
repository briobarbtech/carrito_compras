from django.urls import path
from .views import ProductUpdateView,ProductDeleteView, ProductListView, ProductCreateView, ProductDetailView, agregar_producto,eliminar_producto,limpiar_carrito, restar_producto

app_name='store'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/',ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(),name='product_delete'),
    path('add/<int:producto_id>/', agregar_producto, name='Add'),
    path('del/<int:producto_id>/', eliminar_producto, name='Del'),
    path('sub/<int:producto_id>/', restar_producto, name='Sub'),
    path('cls/', limpiar_carrito, name='CLS'),
    ]