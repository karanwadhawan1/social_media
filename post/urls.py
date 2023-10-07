from django.urls import path
from .views import PostViewSet,FollowerViewSet,LikeViewSet,CommentViewSet,UserFeedViewSet


urlpatterns = [
    path('post', PostViewSet.as_view({'post': 'create'}), name='post'),
    path('all-post', PostViewSet.as_view({'get': 'list'}), name='all-post'),
    path('post/<pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='all-post'),
    path('follow', FollowerViewSet.as_view({'post': 'create'}), name='follow'),
    path('<pk>/unfollow', FollowerViewSet.as_view({'delete':'destroy'}), name='unfollow'),
    path('post/like', LikeViewSet.as_view({'post': 'create'}), name='post-like'),
    path('post/<pk>/unlike', LikeViewSet.as_view({'delete':'destroy'}), name='post-unlike'),
    path('post/comment', CommentViewSet.as_view({'post': 'create'}), name='post-comment'),
    path('user-feed', UserFeedViewSet.as_view({'get': 'list'}), name='user_feed'),
    path('all-comment', CommentViewSet.as_view({'get': 'list'}), name='user_feed'),
     
]