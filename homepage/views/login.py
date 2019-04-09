from django.contrib.auth import authenticate,login
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django import forms
from formlib import Formless
import re

@view_function
def process_request(request):
    
    form = SignupForm(request)

    if form.is_valid():
        # form.commit()
        if(form.username == 'James'):
            return HttpResponseRedirect('/producer')
        elif(form.username == 'Melisa'):
            return HttpResponseRedirect('/manufacturer')
        elif(form.username == 'Leroy'):
            return HttpResponseRedirect('/distributor')
        elif(form.username == 'Michelle'):
            return HttpResponseRedirect('/shipper')
        elif(form.username == 'retailer'):
            return HttpResponseRedirect('/retailer')

    context = {
            'form': form,
        }  

    return request.dmp.render('login.html', context)

class SignupForm(Formless):

    def init(self):
       '''Adds the fields for the form'''
       self.fields['Username'] = forms.CharField(label='Username')
       self.fields['Password'] = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        self.username = self.cleaned_data.get('Username')
        self.password = self.cleaned_data.get('Password')
        # return self.cleaned_data

    def commit(self):
        return HttpResponseRedirect('google.com')
        