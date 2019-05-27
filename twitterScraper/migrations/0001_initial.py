# Generated by Django 2.2.1 on 2019-05-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=500)),
                ('tweet', models.CharField(max_length=500)),
                ('date_collected', models.DateTimeField(auto_now_add=True)),
                ('twitter_user', models.CharField(max_length=50, verbose_name='User Name on Twitter')),
                ('number_of_likes', models.IntegerField()),
                ('number_of_retweets', models.IntegerField()),
                ('tweet_device', models.CharField(blank=True, max_length=50, null=True, verbose_name='Device Tweet was collected from')),
            ],
            options={
                'ordering': ('tweet_id',),
            },
        ),
    ]
