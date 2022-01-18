from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Car, PostedComment, PostedQuote
from .serializers import CarSerializer, PostedCommentSerializer, PostedQuoteSerializer, ApiCommentSerializer, ApiComment
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class CarList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['POST', "GET"])
@permission_classes([IsAuthenticated])
def user_cars(request):

    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        cars = Car.objects.filter(user_id=request.user.id)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def postedQuotes(request):
    if request.method == 'POST':
        serializer = PostedQuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        quotes = PostedQuote.objects.filter(user_id=request.user.id)
        serializer = PostedQuoteSerializer(quotes, many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":  
        record = PostedQuote.first()
        record.delete()
        print("Record deleted successfully!")



@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def postedComment(request):
    if request.method == 'POST':
        serializer = PostedCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        comments = PostedComment.objects.filter(user_id=request.user.id)
        serializer = PostedCommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        PostedQuote.objects.filter(id=id).delete()
        return Response("Comment Deleted")

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def apiComment(request):
    if request.method == 'POST':
        serializer = ApiCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        comments = ApiComment.objects.filter(user_id=request.user.id)
        serializer = ApiCommentSerializer(comments, many=True)
        return Response(serializer.data)




@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_postedQuotes(request):
    quotes = PostedQuote.objects.all()
    serializer = PostedQuoteSerializer(quotes, many=True)
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_postedComments(request):
    comments = PostedComment.objects.all()
    serializer = PostedCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_apiComments(request):
    comments = ApiComment.objects.all()
    serializer = ApiCommentSerializer(comments, many=True)
    return Response(serializer.data)




@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def userFavorite(request):
    if request.method == 'POST':
        serializer = UserFavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        favoriteQuote = UserFavorite.objects.filter(user_id=request.user.id)
        serializer = UserFavoriteSerializer(comments, many=True)
        return Response(serializer.data)




# DELETE

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteComment(request, pk):
    if request.method == 'DELETE':
        snippet = PostedComment.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteQuote(request, pk):
    if request.method == 'DELETE':
        snippet = PostedQuote.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
