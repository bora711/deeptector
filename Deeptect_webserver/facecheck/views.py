from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Member,D1,D2
from .serializer import D1Serializer,D2Serializer,memberSerializer


# Create your views here.

def get_member(request):
    datalist = Member.objects.all()
    print(datalist)
    if request.method == 'GET':
        # print("test=====")
        serializer = memberSerializer(datalist, many=True)
        # print(serializer)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': True})


def get_D1(request):
    datalist = D1.objects.all()
    print(datalist)
    if request.method == 'GET':
        # print("test=====")
        serializer = D1Serializer(datalist, many=True)
        # print(serializer)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_D2(request):
    datalist = D2.objects.all()
    print(datalist)
    if request.method == 'GET':
        # print("test=====")
        serializer = D2Serializer(datalist, many=True)
        # print(serializer)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})