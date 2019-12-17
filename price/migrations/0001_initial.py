# Generated by Django 2.0.4 on 2018-05-25 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0021_auto_20180525_0751'),
        ('device', '0007_auto_20180525_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_cost', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Unit cost')),
                ('system_cost', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='System cost')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Discount name')),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('cost_type', models.PositiveSmallIntegerField(choices=[(1, 'Unit cost'), (2, 'System cost')], verbose_name='Type')),
                ('client_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.ClientPrice')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='discount',
            unique_together={('name', 'cost_type', 'client_price')},
        ),
        migrations.AlterUniqueTogether(
            name='clientprice',
            unique_together={('product', 'client')},
        ),
    ]
