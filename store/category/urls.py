from django.urls import path
from .views import (
    CategoryListCreate,
    CategoryRetrieveUpdateDestroy,
)


urlpatterns = [
    path(
        'category/',
        CategoryListCreate.as_view(),
        name='category'
    ),
    path(
        'category/<int:pk>',
        CategoryRetrieveUpdateDestroy.as_view(),
        name='category'
    ),

]
