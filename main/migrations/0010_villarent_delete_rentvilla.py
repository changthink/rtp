# Generated by Django 4.1.7 on 2023-04-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_rentvilla_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillaRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('광역시도', models.TextField(blank=True, null=True)),
                ('시자치구', models.TextField(blank=True, null=True)),
                ('법정동', models.TextField(blank=True, null=True)),
                ('단지명', models.TextField(blank=True, null=True)),
                ('전용면적', models.FloatField(blank=True, null=True)),
                ('전용', models.IntegerField(blank=True, null=True)),
                ('보증금', models.IntegerField(blank=True, null=True)),
                ('월세', models.IntegerField(blank=True, null=True)),
                ('층', models.IntegerField(blank=True, null=True)),
                ('년', models.IntegerField(blank=True, null=True)),
                ('월', models.IntegerField(blank=True, null=True)),
                ('기준월', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'villa_rent',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='RentVilla',
        ),
    ]
