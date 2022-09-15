from legal.services import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib import messages

from .services import *

from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import io
import json
from rest_framework.decorators import api_view


# Create your views here.
@csrf_exempt
@api_view(['GET','POST','PUT'])
def Legal_vegeata_views(request,id):
    if request.method == 'GET':
        try:
           
            print("Inside collapp -> Legal GET")
            legal_data = get_legal_mst(id)
            return HttpResponse(legal_data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
    
    elif request.method == 'POST':
        try:
           
            print("Inside collapp -> legal POST")
            data = post_legal_mst(request)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
    
    else :

        raise Exception("Invalid Method")

@csrf_exempt
@api_view(['GET','POST','PUT'])
def Collapp_mst_views(request,id):
    if request.method == 'GET':
        try:
           
            print("Inside Collapp")
            data = get_collapp_mst(id)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
            

# Create your views here.
