from django.template import Library

register = Library()

def last_modified(the_date_time):
    return {'value': the_date_time}

def last_modified_short(the_date_time):
    return {'value': the_date_time}

def tag_list(tags):
    return {'value': tags}

def comments_count(object):
    return {'value': object}

@register.filter("truncate_chars") 
def truncate_chars(value, max_length):  
    if len(value) > max_length:  
        truncd_val = value[:max_length]  
        if value[max_length+1] != " ":  
            truncd_val = truncd_val[:truncd_val.rfind(" ")]  
        return  truncd_val + "..."  
    return value  

register.inclusion_tag('core/last_modified.html')(last_modified)
register.inclusion_tag('core/last_modified_short.html')(last_modified_short)
register.inclusion_tag('core/tag_list.html')(tag_list)
register.inclusion_tag('core/comments.html')(comments_count)
