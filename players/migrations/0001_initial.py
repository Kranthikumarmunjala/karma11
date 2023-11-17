# Generated by Django 4.1.5 on 2023-11-17 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('runs', models.IntegerField(blank=True, null=True)),
                ('matches', models.IntegerField(blank=True, null=True)),
                ('wickets', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('batting_style', models.CharField(blank=True, choices=[('Left-hand bat', 'Left-hand bat'), ('Right-hand bat', 'Right-hand bat')], max_length=255, null=True)),
                ('bowling_style', models.CharField(blank=True, choices=[('Right-arm fast', 'Right-arm fast'), (' Left-arm fast', 'Left-arm fast'), ('Right-arm medium', 'Right-arm medium'), ('Left-arm medium', 'Left-arm medium'), ('Right-arm ofbreak', 'Right-arm ofbreak'), ('Left-arm ofbreak', 'Left-arm ofbreak'), ('Right-arm fast-medium', 'Right-arm fast-medium'), ('Left-arm fast-medium', 'Left-arm fast-medium')], max_length=255, null=True)),
                ('player_type', models.CharField(blank=True, choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('Allrounder', 'Allrounder'), ('Wicketkeeper', 'Wicketkeeper')], max_length=255, null=True)),
                ('is_captain', models.BooleanField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countries.country')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerMatchPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matches.match')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.player')),
            ],
        ),
    ]
