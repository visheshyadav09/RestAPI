from django.shortcuts import render

from django.http import HttpResponse,Http404

from .models import Post

from .serializers import PostSerializer

from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PostList(APIView):
    'List all the posts'

    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def get(self,request,format=None):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

class PostDetails(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


    def get_post(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        post=self.get_post(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)


    def put(self,request,pk,format=None):
        post=self.get_post(pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        post=self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)