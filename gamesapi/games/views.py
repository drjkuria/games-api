from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions

from games.models import Game
from games.models import GameCategory
from games.serializers import GameSerializer
from games.serializers import GameCategorySerializer
from games.serializers import UserSerializer
from games.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

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

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'games': reverse(GameList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            })
