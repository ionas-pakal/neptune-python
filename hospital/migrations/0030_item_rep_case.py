# Generated by Django 2.0.4 on 2018-06-29 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
        ('hospital', '0029_auto_20180626_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rep_case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.RepCase'),
        ),
    ]