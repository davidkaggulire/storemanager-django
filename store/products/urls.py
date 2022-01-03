from django.urls import path
from .views import (
    ProductListCreate,
    ProductRetrieveUpdateDestroy,
)


urlpatterns = [
    path(
        'products/',
        ProductListCreate.as_view(),
        name='products'
    ),
    path(
        'products/<int:pk>',
        ProductRetrieveUpdateDestroy.as_view(),
        name='products'
    ),

]
