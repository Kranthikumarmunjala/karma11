"""karma11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from countries.views import all_countries,country
from players.views import all_players,player
from matches.views import matches,match
from teams.views import all_teams,team
from users.views import all_users,user
from leaderboard.views import leaderboards,leaderboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_countries/',all_countries),
    path('country/',country),
    path('all_players/',all_players),
    path('player/',player),
    path('matches/',matches),
    path('match/',match),
    path('all_teams/',all_teams),
    path('team/',team),
    path('all_users/',all_users),
    path('user/',user),
    path('leaderboards/',leaderboards),
    path('leaderboard/',leaderboard),
]
