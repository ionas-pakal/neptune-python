# Generated by Django 2.0.4 on 2018-05-17 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': ' Categories'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name_plural': '  Specialties'},
        ),
    ]