# Generated by Django 3.2.4 on 2021-08-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read the complete document', max_length=255),
        ),
    ]
