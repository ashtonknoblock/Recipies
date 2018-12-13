from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebook.models import Recipe, Person

from recipebook.forms import recipe_add_form, author_add_form, LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required


def recipe_list_view(request):

    results = Recipe.objects.all()
    return render(request, 'recipe_list_view.html', {'data': results})


def recipe_details(request, recipe_pk):

    filtered_result = Recipe.objects.all().filter(id=recipe_pk)
    recipe_id = filtered_result.values()[0]['id']
    author_id = filtered_result.values()[0]['author_id']
    people = Person.objects.all().values()

    for item in people:
        if item['id'] == author_id:
            author = item['name']
            author_id = item['id']
            bio = item['bio']


    return render(request, 'recipe_details.html', {'title': filtered_result.values()[0]['title'],
                                                    'description': filtered_result.values()[0]['description'],
                                                    'time': filtered_result.values()[0]['time_required'],
                                                    # 'instructions': filtered_result.values()[0]['instructions'],
                                                    'author': author,
                                                    'recipe_id': filtered_result.values()[0]['id'],
                                                    'author_id': author_id,
                                                    'bio': bio})


def author_detail(request, author_pk):

    people = Person.objects.all().values()

  
    results = Recipe.objects.filter(author_id=author_pk)


    return render(request, 'author_detail.html', {'data': results,
                                                'author': people.values()[id - 1]['name'],
                                                'bio': people.values()[id - 1]['bio']})
@login_required()
def recipe_add(request):
    html = 'recipe_add.html'
    form = None

    if request.method == 'POST':
        #Take the info from the POST and shove it in the db
        form = recipe_add_form(request.user,request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                title = data['title'],
                author = Person.objects.filter(id=data['author']).first() ,
                description = data['description'],
                time_required = data['time_required']
            )

            return render(request, 'thanks.html')

    else:
        #everything else will be a GET request
        form = recipe_add_form(user = request.user)

    return render(request, html, {'form': form})

@staff_member_required()
def author_add(request):
    html = 'author_add.html'
    form = None

    if request.method == 'POST':
        #Take the info from the POST and shove it in the db
        pass
        form = author_add_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Person.objects.create(
                name = data['name'],
                bio = data['bio'],
            )

            return render(request, 'thanks.html')


    else:
        #everything else will be a GET request
        form = author_add_form()

    return render(request, html, {'form': form})


def signup_view(request):
    html = 'signup.html'

    form = SignupForm(None or request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(
            data['username'], data['email'], data['password'])
        login(request, user)
        return HttpResponseRedirect(reverse('homepage'))
        
    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'

    form = LoginForm(None or request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(username=data['username'],password=data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')