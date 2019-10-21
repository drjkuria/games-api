from rest_framework import serializers

from games.models import GameCategory
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
        slug_field='name')

    class Meta:
        model = Game
        fields = (
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
