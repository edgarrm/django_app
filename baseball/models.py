from django.db import models


class Coach(models.Model):
    #Coach model
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Coaches'

    def __unicode__(self):
        return u"{name}".format(name=self.name)
