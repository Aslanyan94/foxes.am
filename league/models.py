from django.db import models


class MadScheduleAndResults2021(models.Model):
    game_dt = models.DateTimeField(verbose_name="Game Date")
    team1 = models.CharField(verbose_name="Team1", max_length=25)
    team2 = models.CharField(verbose_name="Team2", max_length=25)
    score = models.CharField(verbose_name="Game Score", max_length=15)
    place = models.CharField(verbose_name="Game Place", max_length=25)

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "Mad Game 20-21"
        verbose_name_plural = "Mad Games 20-21"


class LesScheduleAndResults2021(models.Model):
    game_dt = models.DateTimeField(verbose_name="Game Date")
    team1 = models.CharField(verbose_name="Team1", max_length=25)
    team2 = models.CharField(verbose_name="Team2", max_length=25)
    score = models.CharField(verbose_name="Game Score", max_length=15)
    place = models.CharField(verbose_name="Game Place", max_length=25)

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "Les Game 20-21"
        verbose_name_plural = "Les Games 20-21"


class MadScheduleAndResults2122(models.Model):
    game_dt = models.DateTimeField(verbose_name="Game Date")
    team1 = models.CharField(verbose_name="Team1", max_length=25)
    team2 = models.CharField(verbose_name="Team2", max_length=25)
    score = models.CharField(verbose_name="Game Score", max_length=15)
    place = models.CharField(verbose_name="Game Place", max_length=25)

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "Mad Game 21-22"
        verbose_name_plural = "Mad Games 21-22"


class LesScheduleAndResults2122(models.Model):
    game_dt = models.DateTimeField(verbose_name="Game Date")
    team1 = models.CharField(verbose_name="Team1", max_length=25)
    team2 = models.CharField(verbose_name="Team2", max_length=25)
    score = models.CharField(verbose_name="Game Score", max_length=15)
    place = models.CharField(verbose_name="Game Place", max_length=25)

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "Les Game 21-22"
        verbose_name_plural = "Les Games 21-22"
