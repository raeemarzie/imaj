from rest_framework import serializers
from blog.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title']



class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    # def get_image(self, obj):
    #     if obj.image is None:
    #         return obj.image
    #     return MinioClient().get_link(f"image_staff/{obj.username}")

    class Meta:
        model = Post
        fields = ['id', 'category' , 'title', 'body', 'caption', 'meta_description', 'keywords', "date_created",
                  "date_modified", 'publish_date', 'published', 'main_image', 'header_image']


