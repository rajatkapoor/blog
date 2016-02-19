from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import serializers

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

@receiver(pre_save, sender=Comment)
def validate_comment(sender, instance, **kwargs):
    if instance.paragraphNumber > len(instance.blog.paragraphs) or instance.paragraphNumber<1:
        raise serializers.ValidationError("Paragraph Number invalid")
