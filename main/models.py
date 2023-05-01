from django.db import models

class Web(models.Model):
    id = models.IntegerField(primary_key=True)
    pw = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web'

class Bunyang(models.Model):
    시군구 = models.TextField(blank=True, null=True)
    지역코드 = models.BigIntegerField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.BigIntegerField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    구분 = models.TextField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bunyang'


class SaleSma(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.TextField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_sma'

class SaleBig6(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.TextField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_big6'

class SaleDodo(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.TextField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_dodo'

class VillaSale(models.Model):
    시군구 = models.TextField(blank=True, null=True)
    지역코드 = models.BigIntegerField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    단지명 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.BigIntegerField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    대지권면적 = models.FloatField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'villa_sale'

class RentSma(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    보증금 = models.BigIntegerField(blank=True, null=True)
    월세 = models.BigIntegerField(blank=True, null=True)
    층 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rent_sma'

class RentNotsma(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    보증금 = models.BigIntegerField(blank=True, null=True)
    월세 = models.BigIntegerField(blank=True, null=True)
    층 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rent_notsma'


class VillaRent(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    단지명 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    보증금 = models.BigIntegerField(blank=True, null=True)
    월세 = models.BigIntegerField(blank=True, null=True)
    층 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villa_rent'
