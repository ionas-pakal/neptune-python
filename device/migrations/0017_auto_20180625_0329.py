# Generated by Django 2.0.4 on 2018-06-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0016_auto_20180622_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='value',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Feature value'),
        ),
    ]