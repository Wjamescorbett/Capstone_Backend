from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

class PostedQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quoteText = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    keyWord = models.CharField(max_length=20)
    comments = models.CharField(max_length=500)

class PostedComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postedQuote = models.ForeignKey(PostedQuote, on_delete=models.CASCADE)
    commentText = models.CharField(max_length=500)

class ApiComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apiQuote = models.CharField(max_length=500)
    commentText = models.CharField(max_length=500)




class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postedQuote = models.ForeignKey(PostedQuote, on_delete=models.CASCADE)