from django.urls import path
from .views import * 

urlpatterns = [
    path('', map, name='map'),
    path('getData/', getData.as_view(), name='getData'),
    path('setData/', setData.as_view(), name='setData'),

]