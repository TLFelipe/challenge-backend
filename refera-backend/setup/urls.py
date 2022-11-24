from django.contrib import admin
from django.urls import path, include
from table.views import OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders', OrderViewSet, basename='Orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
