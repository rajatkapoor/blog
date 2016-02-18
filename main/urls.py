from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = patterns('',
	url(r'^api/blogs/$',views.BlogList.as_view()),
	url(r'^api/blogs/(?P<pk>[0-9]+)$',views.BlogDetails.as_view()),
	url(r'^api/comments/$',views.CommentList.as_view()),
	url(r'^api/comments/(?P<pk>[0-9]+)$',views.CommentDetails.as_view()),
	)
urlpatterns = format_suffix_patterns(urlpatterns)