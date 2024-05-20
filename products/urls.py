
from django.urls import path
from products.views import products, search_products, product_detail


app_name = 'products'

urlpatterns = [
  path('', products, name='index'),
  path('category/<int:category_id>/', products, name='category'),
  path('educationFormat/<int:educationFormat_id>/', products, name='educationFormat'),
  path('transEducation/<int:transEducation_id>/', products, name='transEducation'),
  path('search/', search_products, name='search'),
  path('product/<int:pk>/', product_detail, name='product_detail'),
]
