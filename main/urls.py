from django.urls import include, path
from . import views #views.py import

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/search/', views.search, name="search"),
    path('main/rprice/', views.rprice, name="rprice"),


    path('main/bunyang', views.bunyang, name='bunyang'),
    path('main/sale_sma', views.sale_sma, name='sale_sma'),
    path('main/pivot_view', views.pivot_view, name='pivot_view'),
    # path('main/sale_sma2', views.sale_sma2, name='sale_sma2'),
    # path('main/sale_dodo', views.sale_dodo, name='sale_dodo'),
    # path('main/sale_big6', views.sale_big6, name='sale_big6'),
    path('main/villa_sale', views.villa_sale, name='villa_sale'),
    # path('post', views.post_index),
    # path('main/dbconn', views.dbconn),

    # path('main/ot_sale', views.ot_sale, name='ot_sale'),

    ]