from django.template import Library
from django.conf import settings 
register = Library()

MEDIA_URL = settings.__getattr__('MEDIA_URL')

def read_more(link, object_id):
    return "<p><img src=\""+MEDIA_URL+"jpg/arrow.png\"/><a href=\"%s%s\">Read more</a></p>" % (link, object_id)

def visit(link):
    return "<p><img src=\""+MEDIA_URL+"jpg/arrow.png\"/><a target=\"_blank\" href=\"%s\">Visit</a></p>" % (link)

def edit(link, object_id):
    return "<p><img src=\""+MEDIA_URL+"jpg/arrow.png\"/><a target=\"_blank\" href=\"%s%s\">Edit</a></p>" % (link, object_id)

def delete(link, object_id):
    return "<p><img src=\""+MEDIA_URL+"jpg/arrow.png\"/><a target=\"_blank\" href=\"%s%s/delete\">Delete</a></p>" % (link, object_id)

def link():
    return "<img src=\""+MEDIA_URL+"jpg/arrow.png\"/>"

register.simple_tag(read_more)
register.simple_tag(visit)
register.simple_tag(edit)
register.simple_tag(link)
register.simple_tag(delete)
