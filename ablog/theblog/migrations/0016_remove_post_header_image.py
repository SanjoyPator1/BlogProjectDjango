# Generated by Django 3.2.4 on 2021-08-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0015_post_checkpublic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
    ]
