from blog.models import Post
from rest_framework import filters, status, viewsets
from blog.paginations import CustomPageNumberPagination
from blog.custom_response import CustomResponse
from blog.serializers import *



# Create your views here.
class PostView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Post.objects.all()

    search_fields = ['title', 'body', 'caption', ]
    ordering_fields = ["date_created"]
    http_method_names = ['get']
    pagination_class = CustomPageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        supplier = self.get_object()
        return CustomResponse(data=PostSerializer(supplier).data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        query = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(query)
        ser_data = PostSerializer(page, many=True).data
        return CustomResponse(data=self.get_paginated_response(ser_data).data, status=status.HTTP_200_OK)


