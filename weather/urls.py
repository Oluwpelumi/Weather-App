from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('deletecity/<str:name>', views.deletecity, name='delete')
]
