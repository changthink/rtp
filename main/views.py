from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Max, Avg
import pandas as pd
import openpyxl
from django_pivot.pivot import pivot
# Create your views here.
from .models import Web
from .models import Bunyang, SaleSma, SaleDodo, SaleBig6, VillaSale, RentSma, RentNotsma, VillaRent

def index(request):
    return render(request, 'main/index.html')

def search(request):
    return render(request, 'main/search_form.html')

def rprice(request):
    시도 = request.POST.get("city")
    자치구 = request.POST.get("county")
    조회시작 = request.POST.get("start")
    조회종료 = request.POST.get("end")
    전용B = request.POST.get("size_begin")
    전용E = request.POST.get("size_end")
    check = request.POST.get("gubun")

    if check == '분양권':
        result = Bunyang.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result' : result }
        return render(request, 'main/bunyang.html', data)
    elif check == '매매(수도권)':
        result = SaleSma.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/sale_sma.html', data)
    elif check == '매매(지방)':
        result = SaleBig6.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/sale_big6.html', data)
    elif check == '매매(팔도)':
        result = SaleDodo.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/sale_dodo.html', data)
    elif check == '매매(빌라)':
        result = VillaSale.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/villa_sale.html', data)
    elif check == '전세(수도권)':
        result = RentSma.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/rent_sma.html', data)
    elif check == '전세(비수도권)':
        result = RentNotsma.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/rent_sma.html', data)
    else:
        result = VillaRent.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
        data = {'result': result}
        return render(request, 'main/villa_rent.html', data)



# def rprice_pivot(request):
#     시도 = request.POST.get("city")
#     자치구 = request.POST.get("county")
#     조회시작 = request.POST.get("start")
#     조회종료 = request.POST.get("end")
#     전용B = request.POST.get("size_begin")
#     전용E = request.POST.get("size_end")
#     check = request.POST.get("gubun")
#
#     if check == '분양권':
#         result = Bunyang.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월')
#         pt =pivot(result, ['아파트', '전용'],'거래금액', aggregation=Max)
#         data = {'result' : result }
#         return render(request, 'main/bunyang.html', data)




def bunyang(request):
    result = Bunyang.objects.filter(광역시도='경상남도', 시자치구='김해시', 년='2023')
    data = {'result' : result }
    return render(request, 'main/bunyang.html', data)

def sale_sma(request):
    result = SaleSma.objects.filter(
        광역시도__in=['서울특별시','경기도'],
        전용=59,
        # 전용__gte=59,
        # 전용__lte=85,
        년='2023',
        월='3').order_by('-거래금액')
    data = {
        'result' : result,
            }
    return render(request, 'main/sale_sma.html', data)

def sale_form(request):
    return render(request, 'select_salesma.html')

def sale_sma2(request):
    시도 = request.POST.get("city")
    자치구 = request.POST.get("county")
    조회시작 = request.POST.get("start")
    조회종료 = request.POST.get("end")
    전용B = request.POST.get("size_begin")
    전용E = request.POST.get("size_end")

    # result = Bunyang.objects.filter(광역시도 = 시도, 시자치구 = 자치구,  년='2023')
    result = SaleSma.objects.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E)
    data = {'result' : result }
    return render(request, 'main/sale_sma.html', data)

def sale_dodo(request):
    result = SaleDodo.objects.filter(시자치구='김해시', 년='2023')
    data = {
        'result' : result,
            }
    return render(request, 'main/sale_dodo.html', data)

def sale_big6(request):
    result = SaleBig6.objects.filter(시자치구='부산진구', 년='2023')
    data = {
        'result' : result,
            }
    return render(request, 'main/sale_big6.html', data)

def villa_sale(request):
    result = VillaSale.objects.filter(시자치구='고양시 덕양구', 년='2023')
    data = {'result': result}
    return render(request, 'main/villa_sale.html', data)


def result(request):
    name = request.POST['username']
    students = ['inu', 'james', 'bob']

    if name in students:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'result.html', {'user_name': name, 'is_exist':is_exist})

def dbconn(request):
    result = Web.objects.all()
    data = {'result' : result}
    return render(request, 'main/dbconn.html', data)


def pivot_view(request):
    result = Bunyang.objects.filter(광역시도='경상남도', 시자치구='김해시', 년='2023')
    pivot_table = pivot(result, ['시자치구', '아파트', '전용'], '기준월', '거래금액', aggregation=Max)
    df = pd.DataFrame(pivot_table)
    df.fillna(0, inplace=True)
    # df.to_excel('./temp.xlsx', index=False)
    df.to_clipboard()
    result_html = df.to_html(index=False)
    return HttpResponse(result_html)

    # context = {'pivot': result}
    # return render(request, 'main/pivot_table.html', context)

