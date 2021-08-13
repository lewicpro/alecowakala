# Generated by Django 3.2.6 on 2021-08-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0017_balance_kilichobaki'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='ACB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='AMANA_BANK',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='BOA',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='DCB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='MAENDELEO',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='MKOMBOZI',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='NBC',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='NCARD_CARD',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='NCARD_MACHINE',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='NMB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='TPB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='WESTERN_UNION',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
