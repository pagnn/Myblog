# Generated by Django 2.0 on 2017-12-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20171221_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='findpagnn@gmail.com', max_length=254),
        ),
    ]
