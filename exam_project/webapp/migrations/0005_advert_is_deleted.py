# Generated by Django 3.2.6 on 2021-08-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_advert_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
