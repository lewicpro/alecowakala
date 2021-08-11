# Generated by Django 3.2.6 on 2021-08-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0015_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='balance',
            options={'verbose_name_plural': 'Capital remaining Balance'},
        ),
        migrations.AddField(
            model_name='balance',
            name='AIRTEL_MONEY',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='CRDB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='DTB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='EQUITY',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='HALOPESA',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='HALOPESA_WAKALA_MKUU',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='KCB',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='MPESA_ACTIVE',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='MPESA_FLOAT',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='SELCOM',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='TIGOPESA',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='TIGOPESA_WAKALA_MKUU',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='TTCL',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='access_bank',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='balance',
            name='mkononi',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
