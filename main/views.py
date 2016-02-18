from django.core.paginator import Paginator, EmptyPage
from django.template import Context, Template
from django.http import HttpResponseRedirect, HttpResponse

from rest_framework import generics, pagination
from models import Blog, Comment
from serializers import BlogSerializer, BlogSerializerDetail, CommentSerializer

class BlogPagination(pagination.PageNumberPagination):
    page_size = 5

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BlogPagination

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerDetail

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
