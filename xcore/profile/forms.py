from django import forms
from django.contrib.auth.models import  User
from django.forms import ModelForm, Form
from math_captcha.forms import  MathCaptchaForm
from xcore.profile.models import UserProfile
import re
alnum_re = re.compile(r'^\w+$') # regexp. from jamesodo in #django


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile


class RegistrationForm(MathCaptchaForm):
    username = forms.CharField(label=u'Username', max_length=30)
    email = forms.EmailField(label=u'E-mail address')
    password1 = forms.CharField(label=u'Password',
                                widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label=u'Password (again)',
                                widget=forms.PasswordInput(render_value=False))


    def clean_username(self):
        if not alnum_re.search(self.cleaned_data['username']):
            raise forms.ValidationError(u'Usernames can only contain letters, numbers and underscores')
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(u'This username is already taken. Please choose another.')

    def clean(self):
        super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(u'You must type the same password each time.')
        return self.cleaned_data

    def save(self):
        try:
            new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                                email=self.cleaned_data['email'],
                                                password=self.cleaned_data['password1'])
            new_user.save()
            from django.db import connection
            print connection.queries
            up = UserProfile(user=new_user, url="", country="", email=self.cleaned_data['email'])
            up.save()
        except Exception, e:
            print e
        
        return new_user

    class Meta:
        model = User

