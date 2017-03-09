import re
from django import forms
from login.models import *
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
#use twilio to verify the phone number 
# First, Store "TWILIO_ACCOUNT_SID" and "TWILIO_AUTH_TOKEN" in the environment variables

class RegistrationForm(forms.Form):

  user_id = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("User ID"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
  email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
  phonenumber = forms.RegexField(regex=r'^\d+$',widget=forms.TextInput(attrs=dict(required=True, max_length=15)), label=_("Phone Number"),error_messages={'invalid':_("This value must contain only numbers." )})
  password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=15, render_value=False)), label=_("Password"))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=15, render_value=False)), label=_("Password (again)"))

  def clean_username(self):
      try:
          user = User.objects.get(username=self.cleaned_data['user_id'])
      except User.DoesNotExist:
          return self.cleaned_data['user_id']
      raise forms.ValidationError(_("The user id already exists. Please try another one."))
 
  def clean(self):

    cleaned_data = super(RegistrationForm,self).clean()

    user = User.objects.filter(username=cleaned_data['user_id'])
    if user.exists():
        raise forms.ValidationError(_("The user id already exists. Please try another one."))

    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
      if self.cleaned_data['password1'] != self.cleaned_data['password2']:
        raise forms.ValidationError(_("The two password fields did not match."))

    return cleaned_data
