# Generated by Django 2.0.4 on 2018-08-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0036_auto_20180802_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='not_implanted_reason',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Dropped'), (2, 'Wrong device'), (3, 'Rep error'), (4, 'Doctor error'), (5, 'Damaged packaging')], null=True, verbose_name='Not implanted reason'),
        ),
        migrations.AlterField(
            model_name='item',
            name='expired_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expiry date'),
        ),
    ]
