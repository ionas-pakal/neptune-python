# Generated by Django 2.0.4 on 2018-07-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0019_auto_20180625_0916'),
        ('hospital', '0033_auto_20180705_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='specialties',
            field=models.ManyToManyField(to='device.Specialty'),
        ),
    ]