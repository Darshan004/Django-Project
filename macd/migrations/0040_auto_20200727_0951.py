# Generated by Django 3.0.7 on 2020-07-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macd', '0039_auto_20200725_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='values3',
            name='asm_perf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='asm_smp',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='aspshortening_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='aspshortening_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='aspshortening_cfl1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='aspshortening_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='aspshortening_perf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='bibline',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='cpf_d',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='cpf_fr',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='cpf_lv',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='cpf_n',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='hoilh',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='hoilr',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='ieoilb',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='ieoild',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='imcfl2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='imperf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='iscfl2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='isperf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='ls_bibline',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='mp20l',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='mp5and10l',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='nimcfl2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='nimperf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='niscfl2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='nisperf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='petline',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rcno_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rcno_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rcno_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rcno_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhcno_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhcno_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhcno_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhcno_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpko_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpko_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpko_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpko_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkst_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkst_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkst_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkst_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkstl_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkstl_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkstl_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpkstl_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpo_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpo_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpo_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpo_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpoc_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpoc_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpoc_cfl1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpoc_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpoc_perf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpst_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpst_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpst_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhpst_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhsbo_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhsbo_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhsbo_cfl1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhsbo_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rhsbo_perf',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpko_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpko_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpko_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpko_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpst_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpst_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpst_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='rpst_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='shortening_1ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='shortening_2ref',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='shortening_hydro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='shortening_loadout',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='sob_bib',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='sob_d',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='sob_fr',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='sob_h',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='sob_n',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='values3',
            name='sob_perf',
            field=models.FloatField(null=True),
        ),
    ]