# Generated by Django 2.0.4 on 2018-05-23 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_auto_20180516_1013'),
        ('account', '0006_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='hospital.Client'),
        ),
    ]
