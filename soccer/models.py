from django.db import models

# Create your models here.


class Team(models.Model):
    """"

    """
    name = models.CharField(max_length=200)
    coach = models.ForeignKey('Coach', null=True, blank=True)

    def __unicode__(self):
        return u"{name} {coach}".format(name=self.name, coach=self.coach)


class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.team.name)


class Coach(models.Model):
    #Coach model
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Coaches'

    def __unicode__(self):
        return u"{name}".format(name=self.name)
