# Generated by Django 3.0.7 on 2020-07-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macd', '0033_auto_20200723_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='values2',
            name='excprice1a',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values2',
            name='excprice1b',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values2',
            name='excprice1c',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values2',
            name='incprice1a',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values2',
            name='incprice1b',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values2',
            name='incprice1c',
            field=models.FloatField(null=True),
        ),
    ]
