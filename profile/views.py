from django.conf import settings
from django.contrib.comments.signals import comment_will_be_posted
from django.core.mail import mail_admins
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from xcore.profile.forms import RegistrationForm
from xcore.profile.models import UserProfile

import logging
logger = logging.getLogger(__name__)

def register(request):
    # TODO: add django-simple-captcha
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save()
                
                up = UserProfile(user=new_user, url="", country="", email=request.REQUEST['email'])
                up.save()
                
#                subject = " new user: %s" % request.REQUEST['username']
#                msg = "admin-link: /admin/profile/user/"
#                mail_admins(subject, msg, fail_silently=False)
  
                logger.info("user registered")

                # TODO: redirect to /register/complete
                return render_to_response('xcore/register_complete.html', context_instance=RequestContext(request))
                
            except Exception, e:
                # TODO: add log entry
                logger.error(e)
                print "error"
        
       
    else:
        form = RegistrationForm()
    return render_to_response('xcore/register.html', { 'form': form }, context_instance=RequestContext(request))


def server_error(request, template_name='500.html'):
    "Always includes MEDIA_URL"
    from django.http import HttpResponseServerError
    t = loader.get_template(template_name)
    return HttpResponseServerError(t.render(Context({'MEDIA_URL': settings.MEDIA_URL})))


def comment_notification(sender, **kwargs):
    #print "sendmail"
    comment = kwargs['comment']
    subject = ' new comment'
    msg = 'Sender: %s (%s)\n %s\n\nComment:\n%s' % (comment.user_name, comment.user_email, comment.user_url, comment.comment)
    mail_admins(subject, msg, fail_silently=False)

comment_will_be_posted.connect(comment_notification)
