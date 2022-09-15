from tkinter import EXCEPTION
from urllib import request
from django.shortcuts import redirect, render,HttpResponse

from .services import *
from .forms import ArticleForm
from .models import Article
from django.http import HttpResponseRedirect
from django.views import View
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import EmailForm
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
import io
import json
from rest_framework.decorators import api_view

def index(request):
    articles = Article.objects.all()

    return render(request, 'article/index.html', {'articles': articles})

def detail(request):
    article = Article.objects.get(pk=1)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

            return redirect('detail')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'article/detail.html', {'article': article, 'form': form})



@csrf_exempt
@api_view(['GET','POST','PUT'])
def EmailAttachementView(request):
 if request.method=='POST':
    try:
      print(request.data)
      updated_template=get_colapp_mst(request)
      print(updated_template)
      filetest= 'test.html'
    #   return updated_template
      return HttpResponse(updated_template,content_type='application/json')
    except Exception as ex:
        print(ex)





# Create your views here.

# def Legal_vegeata_views(request,id):
#     if request.method == 'GET':
#         try:
           
#             print("Inside collapp -> Legal GET")
#             legal_data = get_legal_mst(id)
#             return HttpResponse(legal_data,content_type='application/json')
#         except Exception as ex:
#             return HttpResponse(ex)
    
#     elif request.method == 'POST':
#         try:
           
#             print("Inside collapp -> legal POST")
#             data = post_legal_mst(request)

#             return HttpResponse(data,content_type='application/json')
#         except Exception as ex:
#             return HttpResponse(ex)
    
#     else :

#         raise Exception("Invalid Method")









    # con=Article.objects.filter(id=i)
    # def get(self, request, *args, **kwargs):
        # 
        # return render(request, self.template_name, {'content': customer})

    # def post(self, request, *args, **kwargs):
    #         f = open(filetest,'r')
    #         filedata = f.read()
    #         f.close()

    #         newdata = filedata.replace(con,con)

    #         f = open(filetest,'w')
    #         f.write(newdata)
    #         f.close()
    #         html_obj=filetest
    #         soup = BeautifulSoup(html_obj)
    #         res=soup.get_text()
    #         print(res)            
    #         subject =res.title 
    #         message = res.content
    #         print(message)
    #         email = ['varshmahale1993@gmail.com']
    #         files = filetest

    #         try:
    #             mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    #             for f in files:
    #                 mail.attach(f.name, f.read(), f.content_type)
    #             mail.send()
    #             return HttpResponse('Your mail has been successfully sent to customer')
    #         except:
    #             return render(request, {'error_message': 'Either the attachment is too big or corrupt'})
