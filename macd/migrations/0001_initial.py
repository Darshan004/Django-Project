# Generated by Django 3.0.6 on 2020-06-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='graphBasedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('hocan', models.FloatField()),
                ('g1sb0', models.FloatField()),
                ('corn', models.FloatField()),
                ('hsbo', models.FloatField()),
                ('stote_oil_blend', models.FloatField()),
                ('chicken_par_fry', models.FloatField()),
            ],
        ),
    ]
