from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

r =DefaultRouter()
r.register("category", CategoryViewSet)
r.register("product", ProductViewSet)


urlpatterns = [
    path('', include(r.urls)),
]
