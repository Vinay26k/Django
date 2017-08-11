from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from FirstApp.models import Topic,WebPage,AccessRecord

def index(request):
    #return HttpResponse("Hello World!")
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    #myDict = {'insert_me':"Hello, Now I'm coming from FirstApp/index.html but still from views.py"}
    return render(request,'FirstApp/index.html',context=date_dict)
