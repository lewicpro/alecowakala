# Generated by Django 3.2.6 on 2021-08-07 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cashin',
            options={'verbose_name_plural': 'Cash In'},
        ),
        migrations.AlterModelOptions(
            name='cashout',
            options={'verbose_name_plural': 'Cash Out'},
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('payment', models.CharField(blank=True, max_length=120, null=True)),
                ('service', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('transactionid', models.CharField(blank=True, max_length=120, null=True)),
                ('officer', models.CharField(blank=True, max_length=120, null=True)),
                ('commission', models.CharField(blank=True, max_length=120, null=True)),
                ('salio', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.ForeignKey(blank=True, max_length=120, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Voucher',
            },
        ),
    ]
