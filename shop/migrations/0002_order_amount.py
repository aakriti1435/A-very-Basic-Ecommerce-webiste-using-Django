# Generated by Django 2.0.6 on 2020-01-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(blank=True, default=0, max_length=100, null=True),
        ),
    ]