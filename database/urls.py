from django.urls import path
from . import views

urlpatterns = [
    path('', views.etl, name='etl'),
    path('extract', views.etl_extract, name='etl_extract'),
    path('transform', views.etl_transform, name='etl_transform'),
    path('load', views.etl_load, name='etl_load'),
    path('manage/nutriscore', views.etl_manage_nutriscore,
         name='etl_manage_nutriscore'),
    path('manage/delete', views.etl_manage_delete, name='etl_manage_delete'),
]
