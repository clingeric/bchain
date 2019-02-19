from django.contrib.auth import authenticate,login
# from account.models import User
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django import forms
import re


@view_function
def process_request(request):

#    form = SignupForm(request)

#    if form.is_valid():
#        form.commit()
#        return HttpResponseRedirect('/')

   context = {
    #    'form': form,
   }

   return request.dmp.render('login.html', context)

# class SignupForm(forms):

#    def init(self):
#        '''Adds the fields for the form'''
#        self.fields['email'] = forms.CharField(label='Email :')
#        self.fields['password'] = forms.CharField(label='Password :', widget=forms.PasswordInput)
#        self.user = None

#    def clean(self):
#        '''Authenticates the user to check for valid credentials'''
#        self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
#        if self.user is None:
#            raise forms.ValidationError('Invalid email or password.')
#        return self.cleaned_data


#    def commit(self):
#        login(self.request, self.user)