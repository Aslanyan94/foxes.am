from django.db import models


# TABLES FOR MAD FOXES

class MadTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    games_played = models.IntegerField(verbose_name="Games")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "Team with Mad Foxes"
        verbose_name_plural = "Teams with Mad Foxes"


class MadPlayers(models.Model):
    player_fullname = models.CharField(max_length=30, verbose_name="Name")
    sh_number = models.IntegerField(verbose_name="Shirt number")
    g_played = models.IntegerField(verbose_name="Games Played")
    position = models.CharField(max_length=20, verbose_name="Position")
    height = models.IntegerField(verbose_name="Height")
    b_date = models.DateField(verbose_name="Birth date")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "Mad player"
        verbose_name_plural = "Mad players"


class MadTopScorer(models.Model):
    player = models.ForeignKey(MadPlayers, on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="points per game")

    def __str__(self):
        return f"{self.player} {self.point}"

    class Meta:
        verbose_name = "Mad Top Scorer"


class MadTopRebounder(models.Model):
    player = models.ForeignKey(MadPlayers, on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="rebounds per game")

    def __str__(self):
        return f"{self.player} {self.point}"

    class Meta:
        verbose_name = "Mad Top Rebounder"


class MadTopAssister(models.Model):
    player = models.ForeignKey(MadPlayers, on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="assists per game")

    def __str__(self):
        return f"{self.player} {self.point}"

    class Meta:
        verbose_name = "Mad Top Assister"


# TABLES FOR LES FOXES

class LesTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    games_played = models.IntegerField(verbose_name="Games")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "Team with Les Foxes"
        verbose_name_plural = "Teams with Les Foxes"


class LesPlayers(models.Model):
    player_fullname = models.CharField(max_length=30, verbose_name="Name")
    sh_number = models.IntegerField(verbose_name="Shirt number")
    g_played = models.IntegerField(verbose_name="Games Played")
    position = models.CharField(max_length=20, verbose_name="Position")
    height = models.IntegerField(verbose_name="Height")
    b_date = models.DateField(verbose_name="Birth date")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "Les player"
        verbose_name_plural = "Les players"


class LesTopScorer(models.Model):
    player = models.ForeignKey(LesPlayers, on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="points per game")

    def __str__(self):
        return f"{self.player} {self.point}"

    class Meta:
        verbose_name = "Les Top Scorer"


class LesTopRebounder(models.Model):
    player = models.ForeignKey(LesPlayers, on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="rebounds per game")

    def __str__(self):
        return f"{self.player} {self.point}"

    class Meta:
        verbose_name = "Les Top Rebounder"


class LesTopAssister(models.Model):
    player = models.ForeignKey(LesPlayers, on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="assists per game")

    def __str__(self):
        return f"{self.player} {self.point}"

    class Meta:
        verbose_name = "Les Top Assister"


# TABLES FOR YOUNG FOXES

class YoungTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    games_played = models.IntegerField(verbose_name="Games")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "Team with Young Foxes"
        verbose_name_plural = "Teams with Young Foxes"


class YoungPlayers(models.Model):
    player_fullname = models.CharField(max_length=30, verbose_name="Name")
    sh_number = models.IntegerField(verbose_name="Shirt number")
    g_played = models.IntegerField(verbose_name="Games Played")
    position = models.CharField(max_length=20, verbose_name="Position")
    height = models.IntegerField(verbose_name="Height")
    b_date = models.DateField(verbose_name="Birth date")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "Young player"
        verbose_name_plural = "Young players"


# TABLES FOR OLD FOXES

class OldTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    games_played = models.IntegerField(verbose_name="Games")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "Team with Old Foxes"
        verbose_name_plural = "Teams with Old Foxes"


class OldPlayers(models.Model):
    player_fullname = models.CharField(max_length=30, verbose_name="Name")
    sh_number = models.IntegerField(verbose_name="Shirt number")
    g_played = models.IntegerField(verbose_name="Games Played")
    position = models.CharField(max_length=20, verbose_name="Position")
    height = models.IntegerField(verbose_name="Height")
    b_date = models.DateField(verbose_name="Birth date")
    pts = models.IntegerField(verbose_name="PTS")
    avg_point = models.IntegerField(verbose_name="Average")

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "Old player"
        verbose_name_plural = "Old players"

# Create your models here.
