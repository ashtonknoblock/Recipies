from django import forms
from recipebook.models import Person

class recipe_add_form(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(recipe_add_form, self).__init__(*args, **kwargs)
        self.fields['author'].choices = [(user.id, user.username)]

    title = forms.CharField(max_length=30)
    authors = [(a.id, a.name) for a in Person.objects.all()]
    author = forms.ChoiceField(choices=authors)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)


class author_add_form(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
