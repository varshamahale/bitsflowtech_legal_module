from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib import messages
from .services import *
from collapp.services import *

from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import io
import json
from rest_framework.decorators import api_view


# Create your views here.
@csrf_exempt
@api_view(['GET','POST','PUT'])
def Legal_views(request,id):
    if request.method == 'GET':
        try:
           
            print("Inside legal")
            data = get_legal_mst(id)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)

    
    
    
    elif request.method == 'POST':
        try:
           
            print("Inside VEGETA POST")
            data = post_legal_mst(request)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)


@csrf_exempt
@api_view(['GET','POST','PUT'])
def Legal_colapp_views(request,id):
    if request.method == 'GET':
        try:
           
            print("Inside Legal")
            data = get_colapp_mst(id)

            return HttpResponse(data,content_type='application/json')
        except Exception as ex:
            return HttpResponse(ex)
            
        

