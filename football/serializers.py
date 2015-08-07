from rest_framework import serializers
from models import Player, Team, Coach


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    
    team_string = serializers.StringRelatedField(source='team.name')

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