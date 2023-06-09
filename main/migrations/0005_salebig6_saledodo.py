# Generated by Django 4.1.7 on 2023-03-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_salesma'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleBig6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('광역시도', models.TextField(blank=True, null=True)),
                ('시자치구', models.TextField(blank=True, null=True)),
                ('법정동', models.TextField(blank=True, null=True)),
                ('아파트', models.TextField(blank=True, null=True)),
                ('전용면적', models.FloatField(blank=True, null=True)),
                ('거래금액', models.BigIntegerField(blank=True, null=True)),
                ('층', models.TextField(blank=True, null=True)),
                ('건축년도', models.BigIntegerField(blank=True, null=True)),
                ('년', models.BigIntegerField(blank=True, null=True)),
                ('월', models.BigIntegerField(blank=True, null=True)),
                ('전용', models.BigIntegerField(blank=True, null=True)),
                ('거래유형', models.TextField(blank=True, null=True)),
                ('기준월', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sale_big6',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SaleDodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('광역시도', models.TextField(blank=True, null=True)),
                ('시자치구', models.TextField(blank=True, null=True)),
                ('법정동', models.TextField(blank=True, null=True)),
                ('아파트', models.TextField(blank=True, null=True)),
                ('전용면적', models.FloatField(blank=True, null=True)),
                ('거래금액', models.BigIntegerField(blank=True, null=True)),
                ('층', models.TextField(blank=True, null=True)),
                ('건축년도', models.BigIntegerField(blank=True, null=True)),
                ('년', models.BigIntegerField(blank=True, null=True)),
                ('월', models.BigIntegerField(blank=True, null=True)),
                ('전용', models.BigIntegerField(blank=True, null=True)),
                ('거래유형', models.TextField(blank=True, null=True)),
                ('기준월', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sale_dodo',
                'managed': False,
            },
        ),
    ]
