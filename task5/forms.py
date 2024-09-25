from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label="Ваше имя")
    password = forms.CharField(min_length=8, label="Ваш пароль")
    password2 = forms.CharField(min_length=8, label="Повторите ваш пароль")
    age = forms.CharField(max_length=3, label="Dаш возраст")
