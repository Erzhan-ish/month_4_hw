from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Укажите почту')
    level = forms.CharField(max_length=15)
    age = forms.IntegerField(required=True, label='Укажите возраст')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Пол')


    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'level',
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.level = self.cleaned_data['level']
            user.age = self.cleaned_data['age']
            user.gender = self.cleaned_data['gender']

            if commit:
                user.save()
            return user