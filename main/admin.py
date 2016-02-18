from django.contrib import admin
from main.models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title',)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('text',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)