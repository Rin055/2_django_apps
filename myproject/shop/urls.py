from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
	path('', views.hello_shop, name='hello_shop'),
]
