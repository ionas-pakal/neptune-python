# Generated by Django 2.0.4 on 2018-07-05 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20180705_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseprice',
            name='counter',
        ),
    ]
