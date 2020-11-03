"""
The render() function takes the request object as its first argument, 
                                template name as its second argument, 
                                dictionary as its optional third argument. 

It returns an HttpResponse object of the given template rendered with the given context.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Player

def home(request):
    players = Player.objects.all()
    return render(request, 'home.html', {'players': players})               # render(request, template, dictionary)

def player_detail(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        raise Http404('Player not found')

    return render(request, 'player_detail.html', {'player': player})        # render(request, template, dictionary)
