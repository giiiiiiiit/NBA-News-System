# Generated by Django 2.2.5 on 2019-09-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_team_news_int'),
    ]

    operations = [
        migrations.CreateModel(
            name='cNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(default=0)),
                ('title_text', models.TextField(max_length=200)),
                ('posttime_text', models.TextField(max_length=200)),
                ('author_text', models.TextField(max_length=200)),
                ('content_text', models.TextField(max_length=200000)),
            ],
        ),
    ]