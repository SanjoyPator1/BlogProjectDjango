# Generated by Django 3.2.4 on 2021-08-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_post_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='checkpublic',
            field=models.CharField(default='public', max_length=255),
        ),
    ]
