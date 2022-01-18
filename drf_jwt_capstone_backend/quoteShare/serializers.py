from rest_framework import serializers
from .models import Car, PostedComment, PostedQuote, UserFavorite, ApiComment

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'user_id']

class PostedQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedQuote
        fields = ['id', 'quoteText', 'author', 'keyWord', 'comments', 'user']

class PostedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedComment
        fields = ['id', 'postedQuote', 'commentText', 'user']

class ApiCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiComment
        fields = ['id', 'apiQuote', 'commentText', 'user']

class UserFavoriteSerializer(serializers.ModelSerializer):
    model = UserFavorite
    fields = ['id', 'postedQuote', 'user_id']