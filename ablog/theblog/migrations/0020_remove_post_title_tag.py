# Generated by Django 3.2.4 on 2021-08-07 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0019_author_book_post1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
