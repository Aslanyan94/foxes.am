from django.db import models

# Mad Foxes

class MadRoster(models.Model):
    pl_name = models.CharField(max_length=35,verbose_name="Name")
    position = models.CharField(max_length=20,verbose_name="Position")
    height = models.CharField(max_length=10,verbose_name="Height")
    b_date = models.DateField(verbose_name="Birth Date")

    def __str__(self):
        return f"{self.pl_name}"

    class Meta:
        verbose_name = "Mad Player's Roster"
        verbose_name_plural = "Mad Players's Rosters"


# Les Foxes

class LesRoster(models.Model):
    pl_name = models.CharField(max_length=35, verbose_name="Name")
    position = models.CharField(max_length=20, verbose_name="Position")
    height = models.CharField(max_length=10, verbose_name="Height")
    b_date = models.DateField(verbose_name="Birth Date")

    def __str__(self):
        return f"{self.pl_name}"

    class Meta:
        verbose_name = "Les Player's Roster"
        verbose_name_plural = "Les Players's Rosters"
