from rest_framework import serializers
from .models import Car, PostedComment, PostedQuote

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'user_id']

class PostedQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedQuote
        fields = ['id', 'quoteText', 'author', 'keyWord', 'comments']

class PostedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedComment
        fields = ['id', 'commentText']