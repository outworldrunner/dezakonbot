# Generated by Django 3.0 on 2019-12-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zakon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptedzakonmodel',
            name='mailing_status',
            field=models.CharField(default='new', max_length=50),
        ),
        migrations.AddField(
            model_name='registeredzakonmodel',
            name='mailing_status',
            field=models.CharField(default='new', max_length=50),
        ),
    ]
