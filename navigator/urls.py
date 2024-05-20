from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('products', include('products.urls', namespace='products'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


