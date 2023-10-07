from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer,FollowerSerializer,LikeSerializer,CommentSerializer,FeedSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Follow,Like,Comment
from social_media.utility.pagination import CustomPagination


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    
    
    def list(self, request):
        context={}
        queryset = Post.objects.all()
        page = self.paginate_queryset(queryset)
        serializer =FeedSerializer(page, many=True,context={'request': request})
        data =  self.get_paginated_response(serializer.data)
        context['data']=data
        context['message'] = "all posts "
        context['status']=True
        return Response(context, status=status.HTTP_200_OK)

    def create(self, request):
        context={}
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            context['data']=serializer.data
            context['message'] = "post created "
            context['status']=True
            return Response(context, status=status.HTTP_201_CREATED)
        context['data']={}
        context['message'] = serializer.errors
        context['status']=False
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk=None):
        context={}
        try :
            queryset=Post.objects.get(id=pk)
        except :
            context['data']={}
            context['message'] = "post detail not found !"
            context['status']=False
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(queryset,context={'request': request})
        context['data']=serializer.data
        context['message'] = "post data"
        context['status']=True
        return Response(context, status=status.HTTP_200_OK)
    
    
    
class FollowerViewSet(viewsets.ViewSet):
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request):
        context={}
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            context['data']={}
            context['message'] = "the user followed "
            context['status']=True
            return Response(context, status=status.HTTP_201_CREATED)
        context['data']={}
        context['message'] = serializer.errors
        context['status']=False
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        context={}
        try:
            print(request.user)
            user_follower=Follow.objects.get(user__id=pk,followed_by=request.user)
            user_follower.delete()
            context['data']={}
            context['message'] = "the user unfollowed "
            context['status']=True
            return Response(context, status=status.HTTP_200_OK)
        except :
            context['data']={}
            context['message'] = f"Invalid id {pk} - does not exist."
            context['status']=False
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
class LikeViewSet(viewsets.ViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request):
        context={}
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            context['data']={}
            context['message'] = "user like post "
            context['status']=True
            return Response(context, status=status.HTTP_201_CREATED)
        context['data']={}
        context['message'] = serializer.errors
        context['status']=False
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        context={}
        try:
            user_like=Like.objects.get(post__id=pk,user=request.user)
            user_like.delete()
            context['data']={}
            context['message'] = " user unlike post "
            context['status']=True
            return Response(context, status=status.HTTP_200_OK)
        except :
            context['data']={}
            context['message'] = f"Invalid id {pk} - does not exist."
            context['status']=False
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    
    
    def list(self, request):
        context={}
        queryset = Comment.objects.all()
        page = self.paginate_queryset(queryset)
        serializer =self.serializer_class(queryset, many=True,context={'request': request})
        data =  self.get_paginated_response(serializer.data)
        context['data']=data
        context['message'] = "all comments "
        context['status']=True
        return Response(context, status=status.HTTP_200_OK)


    def create(self, request):
        context={}
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            context['data']={}
            context['message'] = "user comment on post "
            context['status']=True
            return Response(context, status=status.HTTP_201_CREATED)
        context['data']={}
        context['message'] = serializer.errors
        context['status']=False
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
class UserFeedViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def list(self, request):
        context={}
        following_users =request.user.followed_by.all().values_list('followed_by', flat=True)
        feed_posts = Post.objects.filter(user__in=following_users).order_by('-created_at')
        page = self.paginate_queryset(feed_posts)
        serializer = FeedSerializer(page, many=True)
        data =  self.get_paginated_response(serializer.data)
        context['data']=data
        context['message'] = "all userfeed detail"
        context['status']=True
        return Response(context, status=status.HTTP_200_OK)