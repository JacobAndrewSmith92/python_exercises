# Generated by Django 2.0.7 on 2018-07-19 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100)),
                ('year_started', models.CharField(default='2018', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('release_year', models.CharField(default='2010', max_length=4)),
                ('artist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist')),
            ],
        ),
    ]