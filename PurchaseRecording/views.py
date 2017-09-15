from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    output = {
    }
    return HttpResponse(template.render(output,request))

def credit_card_management(request):
    template = loader.get_template('credmanagement.html')
    output = {
    }
    return HttpResponse(template.render(output, request))

def orders(request):
    template = loader.get_template('orders.html')
    orders = Order.objects.filter().order_by("-order_date")
    output = {
        'order': orders
    }
    return HttpResponse(template.render(output, request))


def gift_card_management(request):
    pass

def get_order_detail():
    pass
