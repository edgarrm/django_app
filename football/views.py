from rest_framework import viewsets
from models import Player, Team, Coach
from football.serializers import PlayerSerializer, TeamSerializer, CoachSerializer


class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CoachViewSet(viewsets.ModelViewSet):

    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
