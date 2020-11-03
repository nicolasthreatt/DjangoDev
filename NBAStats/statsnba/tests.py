"""
Django REST framework has hour types of API test cases:
    - APISimpleTestCase
    - APITransactionTestCase
    - APITestCase
    - APILiveServerTestCase

All of the test case classes implement the same interface as Django's TestCase Class

Remember to use the JSON format when testing API client requests:
    - self.client.post(url, data, format='json')

Info:
    - The Django REST Framework extends the interface of the HTTP client that Django uses for unit testing.
    - Django REST Framework maintains the same interface for APITestCase and provides additional setup to test the API view/
    - The get and delete HTTP methods are used for testing a generic RetrieveDestroyAPIView rather than the UpdateView.
"""

from django.test import TestCase
from rest_framework.test import APITestCase
import datetime

from django.db import models
from .models import Player


# CreateAPIView Test
class PlayerCreateTestCase(APITestCase):
    def test_create_player(self):
        initial_player_count = Player.objects.count()

        player_attrs = {
            'name'      : 'New Player',
            'jersey_num': 0,
            'team'      : 'CHA',
            'ppg'       : '0.0',
            'fg_p'      : '0.0',
            'tp_p'      : '0.0',
            'reb'       : '0.0',
            'ast'       : '0.0',
            'date'      : '2020-04-03T06:00:00Z',       # Figure out how to get current date
        }

        reponse = self.client.post('/api/players/new', player_attrs)
        if(reponse.status_code != 201):
            print(reponse.data)

        self.assertEqual(
            Player.objects.count(),
            initial_player_count + 1,
        )

        for attr, expected_value in player_attrs.items():
            self.assertEqual(reponse.data[attr], expected_value)


"""
Test that cleanup methods are excited when destroying the model through the API.
For example, clear caches, destroy the object in other third-party services.
"""
class PlayerDestroy(APITestCase):
    def test_delete_player(self):
        initial_player_count = Player.objects.count()
        player_id            = Player.objects.first()     # Figure out how to get id

        self.client.delete('/api/players/{}/'.format(player_id))
        self.assertEqual(
            Player.objects.count(),
            initial_player_count - 1,
        )

        self.assertRaises(
            Player.DoesNotExist,
            Player.objects.get, id=player_id,
        )

class PlayerListTestCase(APITestCase):
    def test_list_players(self):
        player_count = Player.objects.count()

        reponse = self.client.get('/api/players/')
        self.assertIsNone(reponse.data['next'])
        self.assertIsNone(reponse.data['previous'])
        self.assertEqual(reponse.data['count'], player_count)
        self.assertEqual(len(reponse.data['results']), player_count)

class PlayerUpdateTestCase(APITestCase):
    def test_update_player(self):
        player = Player.objects.first()

        reponse = self.client.patch(
            '/api/players/{}/'.format(player.id),           # Figure out how to get id
            {
                'name'      : 'Updated Player',
            },
            format='json'
        )

        updated = Player.objects.get(id=player.get('pk'))

        self.assertEqual(updated.name, 'Updated Player')


