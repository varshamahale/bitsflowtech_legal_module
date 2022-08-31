from django.shortcuts import render
from legal.services import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib import messages

from .services import get_colapp_mst

from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import io
import json
from rest_framework.decorators import api_view


# Create your views here.
@csrf_exempt
@api_view(['GET','POST','PUT'])
def Colapp_legal_views(request,id):
    if request.method == 'GET':
        try:
           
            print("Inside colapp -> Legal GET")
            legal_data = get_legal_mst(id)
            return HttpResponse(legal_data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
    
    elif request.method == 'POST':
        try:
           
            print("Inside colapp -> legal POST")
            data = post_legal_mst(request)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
    
    else :

        raise Exception("Invalid Method")

@csrf_exempt
@api_view(['GET','POST','PUT'])
def Colapp_mst_views(request,id):
    if request.method == 'GET':
        try:
           
            print("Inside Colapp")
            data = get_colapp_mst(id)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
            

# Create your views here.
