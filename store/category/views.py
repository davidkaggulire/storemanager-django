# category views 

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"category":serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_one_product(self, category_id):
        category = generics.get_object_or_404(Category, id=category_id)
        return category

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product = self.get_one_product(kwargs.pop('pk'))
        product.delete()
        return Response(
            {
                "message": "Category has been successfully deleted"
            },
            status=status.HTTP_200_OK
        )
