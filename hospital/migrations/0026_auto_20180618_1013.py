# Generated by Django 2.0.4 on 2018-06-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0025_auto_20180615_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='item',
            name='cost_type',
        ),
        migrations.AddField(
            model_name='item',
            name='system_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='item',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
