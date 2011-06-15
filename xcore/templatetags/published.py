from django.template import Library

register = Library()


def is_published(object_id):
    rc=""
    if object_id.published == 1:
	rc=""
    elif object_id.published == 0:
        rc="not_published" 
    return rc

register.simple_tag(is_published)
