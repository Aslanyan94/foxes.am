from django.db import models


# TABLES FOR MAD FOXES

class MadTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    avg_point = models.IntegerField()

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "team(Mad)"
        verbose_name_plural = "teams(Mad)"


class MadPlayers(models.Model):
    player_fullname = models.CharField(max_length=50, verbose_name="Player")
    team = models.ForeignKey("MadTeam", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "player(Mad)"
        verbose_name_plural = "players(Mad)"


class MadMatches(models.Model):
    team1 = models.ForeignKey(MadTeam, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(MadTeam, on_delete=models.CASCADE, related_name='team2')
    t1_result = models.IntegerField(verbose_name="team1 result", default=0)
    t2_result = models.IntegerField(verbose_name="team2 result",default=0)
    m_time = models.DateField(verbose_name="Match Time")

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "match(Mad)"
        verbose_name_plural = "matches(Mad)"


#  TABLES FOR LES FOXES

class LesTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    avg_point = models.IntegerField()

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "team(Les)"
        verbose_name_plural = "teams(Les)"


class LesPlayers(models.Model):
    player_fullname = models.CharField(max_length=50, verbose_name="Player")
    team = models.ForeignKey("MadTeam", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "player(Les)"
        verbose_name_plural = "players(Les)"


class LesMatches(models.Model):
    team1 = models.ForeignKey(LesTeam, on_delete=models.CASCADE, related_name='team_1')
    team2 = models.ForeignKey(LesTeam, on_delete=models.CASCADE, related_name='team_2')
    t1_result = models.IntegerField(verbose_name="team1 result",default=0)
    t2_result = models.IntegerField(verbose_name="team2 result",default=0)
    m_time = models.DateTimeField(verbose_name="Match Time")

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "match(Les)"
        verbose_name_plural = "matches(Les)"


#  TABLES FOR YOUNG FOXES

class YoungTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    avg_point = models.IntegerField()

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "team(Young)"
        verbose_name_plural = "teams(Young)"


class YoungPlayers(models.Model):
    player_fullname = models.CharField(max_length=50, verbose_name="Player")
    team = models.ForeignKey("MadTeam", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "player(Young)"
        verbose_name_plural = "players(Young)"


class YoungMatches(models.Model):
    team1 = models.ForeignKey(YoungTeam, on_delete=models.CASCADE, related_name='TeamOne')
    team2 = models.ForeignKey(YoungTeam, on_delete=models.CASCADE, related_name='TeamTwo')
    t1_result = models.IntegerField(verbose_name="team1 result")
    t2_result = models.IntegerField(verbose_name="team2 result")
    m_time = models.DateTimeField(verbose_name="Match Time")

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "match(Young)"
        verbose_name_plural = "matches(Young)"


#  TABLES FOR OLD FOXES

class OldTeam(models.Model):
    team_name = models.CharField(max_length=15, verbose_name="Team")
    avg_point = models.IntegerField()

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "team(Old)"
        verbose_name_plural = "teams(Old)"


class OldPlayers(models.Model):
    player_fullname = models.CharField(max_length=50, verbose_name="Player")
    team = models.ForeignKey("MadTeam", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player_fullname}"

    class Meta:
        verbose_name = "player(Old)"
        verbose_name_plural = "players(Old)"


class OldMatches(models.Model):
    team1 = models.ForeignKey("MadTeam", on_delete=models.CASCADE, related_name='Team_One')
    team2 = models.ForeignKey("MadTeam", on_delete=models.CASCADE, related_name='Team_Two')
    t1_result = models.IntegerField(verbose_name="team1 result")
    t2_result = models.IntegerField(verbose_name="team2 result")
    m_time = models.DateField(verbose_name="Match Time")

    def __str__(self):
        return f"{self.team1} VS {self.team2}"

    class Meta:
        verbose_name = "match(Old)"
        verbose_name_plural = "matches(Old)"

# Create your models here.
