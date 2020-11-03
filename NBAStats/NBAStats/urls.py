"""NBAStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from statsnba import views, api_views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),    # Path to Homepage
    url(r'^statsnba/(\d+)/', views.player_detail, name='player_detail'),
    path('api/players/',    api_views.PlayerList.as_view()),    # Must use path() not url()
    path('api/players/new', api_views.PlayerCreate.as_view()),  # Must use path() not url()
    path('api/players/<int:id>/',  api_views.PlayerRetrieveUpdateDestroy.as_view()),
    path('api/players/<int:id>/stats', api_views.PlayerStats.as_view()),
]