"""
REST API Steps
    1. Data Source
        - Excel Spreadsheet, XML file, JSON file, other databse
    2. Imported through REST API
    3. Populating the Database

Django REST Framework Generic Views
    - ListAPIView
    - CreateAPIView
    - DestroyAPIView
    - RetrieveUpdateDestroyAPIView

SearchFiler
    - Filter back end build into Django REST framework
        i. Types
            a. Partial Match (Default)
            b. Exact Match
            c. Regular Expression

Pagingation
    - PageNumber Pagingation
        a. Use a page number to paginate results
    - LimitOffset Pagination
        a. Use a limit and offset fields to more finely paginate resutls
            1. http://localhost:8000/api/players/?limit=1
            2. localhost:8000/api/players/?limit=2&offset=2
    - Cursor Pagination
        a. Use a database cursor to paginate results
            1. Cursor pagination is the best performance choice for paginating large data sets.
    
Most Cases
    - Use Django REST framework's generic API views and mixins

Rare Cases
    - Use base APIView to build up the API from the ground up
"""

from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from statsnba.serializers import PlayerSerializers, PlayerStatsSerializer
from .models import Player

class PlayersPagination(LimitOffsetPagination):
    default_limit = 10  
    max_limit     = 100

class PlayerList(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', )
    search_fields = ('name', )
    pagination_class = PlayersPagination

    # TOD0: Learn more about filter for greater than or less than
    # Filtering Data in API (http://localhost:8000/api/players/?ppg=20)
    # def get_queryset(self):
    #     ppg = self.request.query_params.get('ppg', None)
    #     if ppg is None:
    #         return super().get_queryset()
    
    #     queryset = Player.objects.all()
    #     if float(ppg) >= 20.0:
    #         return( queryset.filter(ppg__gte=20.0) )    # Filter PPG Greater than 20

    #     return(queryset)

# Create New Player From API (localhost:8000/api/players/new)
class PlayerCreate(CreateAPIView):
    serializer_class = PlayerSerializers

    def create(self, request, *args, **kwargs):

        try:
            ppg = request.data.get('ppg')
            if ppg is not None and float(ppg) < 0.0:
                raise ValidationError({'ppg': 'Must be above 0.0'})
        except ValueError:
            raise ValidationError({'ppg': 'A valid number is required'})

        return(super().create(request, *args, **kwargs))

# Delete Player from API
class PlayerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset         = Player.objects.all()
    serializer_class = PlayerSerializers
    lookup_field     = 'id'

    def delete(self, request, *args, **kwargs):
        player_id = request.data.get('id')

        response = super().delete(request, *args, **kwargs)
        if(response.status_code == 204):
            from django.core.cache import cache
            cache.delete('player_data_{}'.format(player_id))
        return(response)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        if(response.status_code == 200):
            from django.core.cache import cache

            player = response.data
            cache.set('player_data_{}'.format(player.get('id')), {
                'name': player['name'],
                'ppg':  player['ppg'],
                'fg_p': player['fg_p'],
                'tp_p': player['tp_p'],
                'reb':  player['reb'],
                'ast':  player['ast'],
            })

        return(response)

class PlayerStats(GenericAPIView):
    lookup_field = 'id'
    serializer_class = PlayerStatsSerializer
    queryset = Player.objects.all()

    def get(self, request, format=None, id=None):
        obj = self.get_object()
        serializer = PlayerStatsSerializer({
            'stats': {
                'LeBron James':      [25.5, 49.6, 35.0, 7.8, 10.6]
            }
        })
        return(Response(serializer.data))
