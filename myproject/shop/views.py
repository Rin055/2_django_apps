from django.shortcuts import render
from django.http import HttpResponse


def hello_shop(request):
	return HttpResponse("hello from shop app")
