from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.comments.signals import comment_will_be_posted
from django.core.mail import mail_admins
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from xcore.profile.forms import RegistrationForm, UserProfileForm
from django.contrib import auth

import logging
from xcore.profile.models import UserProfile

logger = logging.getLogger("xcore")

def loggedin(request):
    logger.info(str(request.user)+" logged in")
    return render_to_response('xcore/logged_in.html', {}, context_instance = RequestContext(request))

@login_required
def profile(request):

    try:
        prof = request.user.get_profile()
    except Exception, e:
        print e
        from xcore import utils
        utils.print_stacktrace()
        up = UserProfile(user=request.user, url="", country="")
        up.save()
        prof = request.user.get_profile()

    if request.method == 'POST':
        f = UserProfileForm(request.POST, instance=prof)
        if f.is_valid():
            f.save()
            user = User.objects.get(id=request.user.id)
            user.email = request.POST['email']
            user.save()
            return render_to_response('xcore/profile_changed.html', context_instance = RequestContext(request))
    else:
        f = UserProfileForm(instance=prof)

    return render_to_response('xcore/profile.html', {'form': f, 'profile': prof},
        context_instance = RequestContext(request))

def register(request):
    logger.info("register")
    logger.info(request)
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save()
                up = UserProfile(user=new_user, url="", country="", email=request.REQUEST['email'])
                up.save()
                subject = " new user: %s" % request.REQUEST['username']
                msg = "admin-link: /admin/profile/user/"
                mail_admins(subject, msg, fail_silently=True)
                logger.info("user registered")
                return render_to_response('xcore/register_complete.html', {}, context_instance=RequestContext(request))
                
            except Exception, e:
                logger.error("registration failed")
                from xcore import utils
                utils.print_stacktrace()
                new_user.delete()
        else:
            logger.error(form.errors)
            logger.error("invalid")
        
       
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
