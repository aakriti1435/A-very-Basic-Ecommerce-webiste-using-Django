# Generated by Django 2.0.6 on 2020-01-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
