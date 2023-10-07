from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from .models import Post,Follow,Like,Comment



class PostCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ("id",'user','text' ,'created_at')
        extra_kwargs = {"user": {"read_only": True}}
    

    
class PostSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Post
        fields = ('user','title' ,'content' ,'created_at')
        extra_kwargs = {"user": {"read_only": True}}
        
    def get_comments(self,obj):
        return PostCommentSerializer(Comment.objects.filter(post=obj),many=True).data
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = Like.objects.filter(post=instance).count()
        rep['comments'] = self.get_comments(instance)
        return rep

    def create(self, validated_data):    
        return Post.objects.create(user=self.context['request'].user,**validated_data)
    

class  FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id','user','followed_by')
        extra_kwargs = {"followed_by": {"read_only": True}}

    def validate_user(self, value):      
        if Follow.objects.filter(user=value,followed_by=self.context['request'].user).exists():
            raise serializers.ValidationError("user already followed this user")
        return value

    def create(self, validated_data):    
        return Follow.objects.create(followed_by=self.context['request'].user,**validated_data)
    
class  LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','post','user')
        extra_kwargs = {"user": {"read_only": True}}

    def validate_post(self, value):      
        if Like.objects.filter(post=value,user=self.context['request'].user).exists():
            raise serializers.ValidationError("user already like  this post")
        return value

    def create(self, validated_data):    
        return Like.objects.create(user=self.context['request'].user,**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ("id",'user','post' ,'text' ,'created_at')
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):    
        return Comment.objects.create(user=self.context['request'].user,**validated_data)
    
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'