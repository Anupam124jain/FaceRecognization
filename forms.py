from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    firstname = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
                                label=_("firstname"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    lastname = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
                                 label=_("lastname"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))
    mobileno =  forms.RegexField(regex=r'^(?:\+?44)?[07]\d{9,13}$', widget=forms.TextInput(attrs=dict(required=True, max_length=10)),
                                label=_("mobile no."), error_messages={
            'invalid': _("This value must contain only 10 digit.")})
    CHOICES = [('Male','Male'),
               ('Female','Female')]
    gender = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(attrs=dict(required=True, max_length=5)), label=_("gender"))
    #year =  forms.ChoiceField(choices=[x,x] for x in range(1,4))

    # def clean_firstname(self):
    #     try:
    #         user = User.objects.get(firstname__iexact=self.cleaned_data['firstname'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['firstname']
    #     raise forms.ValidationError(_("The firstname already exists. Please try another one."))
    #
    # def clean_lastname(self):
    #     try:
    #         user = User.objects.get(lastname__iexact=self.cleaned_data['lastname'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['lastname']
    #     raise forms.ValidationError(_("The lastname already exists. Please try another one."))

    def clean_mobileno(self):
        try:
            user = User.objects.get(mobileno__iexact=self.cleaned_data['mobileno'])
        except User.DoesNotExist:
            return self.cleaned_data['mobileno']
        raise forms.ValidationError(_("The mobileno. already exists. Please try another one."))



    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))

            def clean_email(self):
                try:
                    user = User.objects.get(email__iexact=self.cleaned_data['email'])
                except User.DoesNotExist:
                    return self.cleaned_data['email']
                raise forms.ValidationError(_("The email already exists. Please try another one."))



