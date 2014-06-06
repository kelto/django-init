# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.Form):
    pass


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()

        return user
