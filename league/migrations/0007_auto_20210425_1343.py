# Generated by Django 3.2 on 2021-04-25 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('our_team', '0001_initial'),
        ('league', '0006_auto_20210424_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALeagueRegular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_lose', models.IntegerField(default=0, verbose_name='W/L')),
                ('point', models.IntegerField(default=0, verbose_name='Points')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegularTeam', to='our_team.madteam')),
            ],
            options={
                'verbose_name': "A-League's team(regular)",
                'verbose_name_plural': "A-League's teams(regular)",
            },
        ),
        migrations.CreateModel(
            name='ALeagueSemifinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_lose', models.IntegerField(default=0, verbose_name='W/L')),
                ('point', models.IntegerField(default=0, verbose_name='Points')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SemifinalTeam', to='our_team.madteam')),
            ],
            options={
                'verbose_name': "A-League's team(semifinal)",
                'verbose_name_plural': "A-League's teams(semifinal)",
            },
        ),
        migrations.CreateModel(
            name='WomenChampionship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_lose', models.IntegerField(default=0, verbose_name='W/L')),
                ('point', models.IntegerField(default=0, verbose_name='Points')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WomenTeam', to='our_team.lesteam')),
            ],
            options={
                'verbose_name': "Women's championship team",
                'verbose_name_plural': "Women's championship teams",
            },
        ),
        migrations.RemoveField(
            model_name='lesmatches',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='lesmatches',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='lesplayers',
            name='team',
        ),
        migrations.RemoveField(
            model_name='madmatches',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='madmatches',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='madplayers',
            name='team',
        ),
        migrations.RemoveField(
            model_name='oldmatches',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='oldmatches',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='oldplayers',
            name='team',
        ),
        migrations.DeleteModel(
            name='OldTeam',
        ),
        migrations.RemoveField(
            model_name='youngmatches',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='youngmatches',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='youngplayers',
            name='team',
        ),
        migrations.DeleteModel(
            name='LesMatches',
        ),
        migrations.DeleteModel(
            name='LesPlayers',
        ),
        migrations.DeleteModel(
            name='LesTeam',
        ),
        migrations.DeleteModel(
            name='MadMatches',
        ),
        migrations.DeleteModel(
            name='MadPlayers',
        ),
        migrations.DeleteModel(
            name='MadTeam',
        ),
        migrations.DeleteModel(
            name='OldMatches',
        ),
        migrations.DeleteModel(
            name='OldPlayers',
        ),
        migrations.DeleteModel(
            name='YoungMatches',
        ),
        migrations.DeleteModel(
            name='YoungPlayers',
        ),
        migrations.DeleteModel(
            name='YoungTeam',
        ),
    ]