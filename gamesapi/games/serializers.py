from rest_framework import serializers

from django.contrib.auth.models import User

from games.models import GameCategory
from games.models import Game
from games.models import Player
from games.models import PlayerScore

class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
        slug_field='name')

    class Meta:
        model = Game
        fields = (
            'owner',
            'game_category',
            'name',
            'release_date',
            'played')

class GameCategorySerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = GameCategory
        fields = (
            'pk',
            'name',
            'games')

class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'games')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()
    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'game',
            )
