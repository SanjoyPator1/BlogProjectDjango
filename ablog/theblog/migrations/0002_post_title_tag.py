# Generated by Django 3.2.4 on 2021-08-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='my blog', max_length=255),
        ),
    ]