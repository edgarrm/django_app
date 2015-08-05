from models import Player, Team, Coach
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team_string = serializers.StringRelatedField(source = 'team.name')
    #team = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = ('url', 'name', 'team', 'team_string')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'name', 'coach')


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('url', 'name')
