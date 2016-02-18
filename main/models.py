from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver

import json
from datetime import datetime   
# Create your models here.

class Blog(models.Model):
    """Model for Blog"""
    title = models.CharField(max_length=500)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now())
    @property
    def paragraphs(self):
        return {k+1:v for k,v in enumerate(self.text.split("\r\n\r\n"))}

    def __unicode__(self):
        return "Blog No. "+str(self.id)+" Title: "+self.title

class Comment(models.Model):
    text = models.TextField()
    paragraphNumber = models.IntegerField(default=1)
    blog = models.ForeignKey('Blog', default=1, related_name="comments")
    time = models.DateTimeField(default=datetime.now())