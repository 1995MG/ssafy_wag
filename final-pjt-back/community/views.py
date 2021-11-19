from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer, CommentListSerializer
from .models import Article, Comment
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_list_create(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes([AllowAny])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # if not request.user.article_set.filter(pk=article_pk).exists():
    #     return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # print(serializer.to_representation(article))
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response({ 'id':article_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_list_create(request, article_pk):

    if request.method == 'GET':
        comments = get_list_or_404(Comment, article_id=article_pk)
        serializers = CommentListSerializer(comments, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response({ 'id':comment_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_likes(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        if user in article.like_users.all():
            liked = True
        else:
            liked = False
        context = {
            'liked': liked,
            'count': article.like_users.count()
        }
        return Response(context)
    elif request.method == 'POST':
        if user in article.like_users.all():
            article.like_users.remove(user)
            liked = False
        else:
            article.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'count': article.like_users.count()
        }
        return Response(context)