# Generated by Django 3.2.6 on 2021-08-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0016_auto_20210811_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='kilichobaki',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
