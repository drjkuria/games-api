from django.contrib import admin

from games.models import Game, GameCategory

admin.site.register(Game)
admin.site.register(GameCategory)
