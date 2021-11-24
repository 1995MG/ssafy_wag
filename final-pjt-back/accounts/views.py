from .models import User
from movies.models import Rank
from community.models import Article, Comment
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from movies.serializers import RankListSerializers
from community.serializers import ArticleListSerializer, CommentListSerializer
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_username(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_rank(request, user_pk):
    ranks = get_list_or_404(Rank, user_id=user_pk)
    serializers = RankListSerializers(ranks, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_article(request, user_pk):
    articles = get_list_or_404(Article, user_id=user_pk)
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_comment(request, user_pk):
    comments = get_list_or_404(Comment, user_id=user_pk)
    serializers = CommentListSerializer(comments, many=True)
    return Response(serializers.data)