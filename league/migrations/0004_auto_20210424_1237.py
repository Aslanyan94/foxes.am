# Generated by Django 3.2 on 2021-04-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_auto_20210424_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesmatches',
            name='m_time',
            field=models.DateTimeField(verbose_name='Match Time'),
        ),
        migrations.AlterField(
            model_name='youngmatches',
            name='m_time',
            field=models.DateTimeField(verbose_name='Match Time'),
        ),
    ]