# Generated by Django 3.2.6 on 2021-08-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0003_inoffice'),
    ]

    operations = [
        migrations.AddField(
            model_name='inoffice',
            name='service',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]