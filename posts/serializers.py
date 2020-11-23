from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ('id', 'author', 'title', 'body', 'created_at',)
        exclude = ('updated_at', 'author', )
        model = Post


