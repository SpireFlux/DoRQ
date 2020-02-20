from django.db import models

# class Player(models.Model):
#     pass

class Replay(models.Model):
    date = models.DateTimeField('date published')
    ladder_map = models.CharField(max_length=200, null=True, blank=True)
    opponent_name = models.CharField(max_length=200, null=True, blank=True)
    opponent_race = models.CharField(max_length=200, null=True, blank=True)
    opponent_league = models.CharField(max_length=200, null=True, blank=True)
    player_name = models.CharField(max_length=200, null=True, blank=True)
    player_race = models.CharField(max_length=200, null=True, blank=True)
    player_league = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)


    # Creep spread %
    # Workers Created
    # MaxTime
    # avg unspent resources
    # time supply capped
    # matchup
