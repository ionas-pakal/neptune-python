# Generated by Django 2.0.4 on 2018-06-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0010_auto_20180604_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Category image'),
        ),
    ]
