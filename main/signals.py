from django.db.models.signals import pre_save
from django.dispatch import receiver

from models import Blog,Comment

import json

@receiver(pre_save, sender=Blog)
def paraSplit(sender, kwargs):
	blog = sender
	blog.paragraphs = json.dumps({k:v for k,v in enumerate(blog.text.replace('\r','\n').split("\n\n"))})
