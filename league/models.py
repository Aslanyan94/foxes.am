from django.db import models
from our_team.models import MadTeam, LesTeam


class ALeagueRegular(models.Model):
    team = models.ForeignKey(MadTeam, on_delete=models.CASCADE, related_name='RegularTeam')
    win = models.IntegerField(verbose_name="Won", default=0)
    lose = models.IntegerField(verbose_name="Lose", default=0)
    point = models.IntegerField(verbose_name="Points", default=0)

    def __str__(self):
        return f"{self.team}"

    class Meta:
        verbose_name = "A-League's team(regular)"
        verbose_name_plural = "A-League's teams(regular)"


class ALeagueSemifinal(models.Model):
    team = models.ForeignKey(MadTeam, on_delete=models.CASCADE, related_name='SemifinalTeam')
    win = models.IntegerField(verbose_name="Won", default=0)
    lose = models.IntegerField(verbose_name="Lose", default=0)
    point = models.IntegerField(verbose_name="Points", default=0)

    def __str__(self):
        return f"{self.team}"

    class Meta:
        verbose_name = "A-League's team(semifinal)"
        verbose_name_plural = "A-League's teams(semifinal)"


#  TABLES FOR LES FOXES


class WomenChampionship(models.Model):
    team = models.ForeignKey(LesTeam, on_delete=models.CASCADE, related_name='WomenTeam')
    win = models.IntegerField(verbose_name="Won", default=0)
    lose = models.IntegerField(verbose_name="Lose", default=0)
    point = models.IntegerField(verbose_name="Points", default=0)

    def __str__(self):
        return f"{self.team}"

    class Meta:
        verbose_name = "Women's championship team"
        verbose_name_plural = "Women's championship teams"
