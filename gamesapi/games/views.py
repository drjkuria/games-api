from django.shortcuts import render

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from games.models import Game
from games.models import GameCategory

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    filter_fields = (
        'name',
        'game_category',
        'release_date',
        'played',)
    search_fields = (
        '^name',)
    ordering_fields = (
        'name',
        'release_date',)

    def perform_create(self, serializer):
        serializer.save()
