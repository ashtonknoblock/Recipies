"""recipebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebook.views import recipe_list_view, recipe_details, author_detail, recipe_add, author_add, login_view, signup_view, logout_view
from recipebook.models import Person, Recipe
from recipebook import settings

admin.site.register(Person)
admin.site.register(Recipe)
app_name = "recipebook"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_list_view, name='homepage'),
    path('recipe/<int:recipe_pk>', recipe_details),
    path('author/<int:author_pk>', author_detail), 
    path('recipe_add/', recipe_add),
    path('author_add/', author_add),
    path('login/', login_view),
    path('signup/', signup_view),
    path('logout/', logout_view, name= 'logout' )
]
