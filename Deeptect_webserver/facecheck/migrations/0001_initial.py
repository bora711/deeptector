# Generated by Django 3.2 on 2021-05-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='D1',
            fields=[
                ('TIME', models.IntegerField(blank=True, db_column='TIME', null=True)),
                ('LOSS', models.FloatField(blank=True, primary_key=True, db_column='LOSS', null=True)),
            ],
            options={
                'db_table': 'D1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='D2',
            fields=[
                ('age_group', models.IntegerField(blank=True, primary_key=True, db_column='age_group', null=True)),
                ('EX_HIGH', models.FloatField(blank=True, db_column='EX_HIGH', null=True)),
                ('EX_MID', models.FloatField(blank=True, db_column='EX_MID', null=True)),
            ],
            options={
                'db_table': 'D2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mask', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('in_enter', models.TimeField(blank=True, null=True)),
                ('bodytemp', models.CharField(blank=True, db_column='bodyTemp', max_length=50, null=True)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
    ]