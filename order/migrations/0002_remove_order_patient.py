# Generated by Django 2.0.4 on 2018-06-21 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='patient',
        ),
    ]