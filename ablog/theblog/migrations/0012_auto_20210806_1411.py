# Generated by Django 3.2.4 on 2021-08-06 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_auto_20210806_1357'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryPP',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoryPP',
        ),
    ]
