from rest_framework import serializers
from models import Blog,Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

class CommentSerializerInsideBlog(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('blog',)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        field = ('id', 'title', 'text')
        exclude = ('time',)

class BlogSerializerDetail(serializers.ModelSerializer):
    comments = CommentSerializerInsideBlog(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'paragraphs' , 'comments', 'time' )
        # exclude = ('text',)
    paragraphs = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()
    def get_paragraphs(self, obj):
        return obj.paragraphs
    # def get_comments(self, obj):
    #     return Comment.objects.get(id=1)

