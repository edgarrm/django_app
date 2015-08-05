from models import Player, Team, Coach
from rest_framework import viewsets
from soccer.serializers import PlayerSerializer, TeamSerializer, CoachSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CoachViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
