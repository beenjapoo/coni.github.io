from django.urls import path
from .views import home,apks,test


urlpatterns = [
    path('', home, name="home"),
    path('apks/<id>', apks, name="apks"),
    path('test/', test, name="test"),
]
