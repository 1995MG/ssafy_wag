# Generated by Django 3.2.9 on 2021-11-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre_ids', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
