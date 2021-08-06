# Generated by Django 3.2.4 on 2021-08-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_post_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categoryPP',
            field=models.CharField(default='private', max_length=255),
        ),
    ]
