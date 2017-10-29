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
    for order in orders:
        order.order_status = order_status_type[order.order_status][1]
    output = {
        'order': orders
    }
    return HttpResponse(template.render(output, request))


def gift_card_management(request):
    pass


def get_order_detail(request, order_id):
    template = loader.get_template('orderdetail.html')
    order_detail = OrderDetail.objects.get(order=order_id)
    print order_detail.order.order_status
    order_detail.order.order_status = order_status_type[order_detail.order.order_status][1]

    output = {
        'order_detail': order_detail
    }

    return HttpResponse(template.render(output, request))


def create_order_record_page(request):
    template = loader.get_template("orderrecord.html")
    merchandiser = Merchandiser.objects.filter()
    output = {
        'merchandisers': merchandiser
    }
    return HttpResponse(template.render(output, request))


def create_record(request):
    order_name = request.POST.get('orderName', None)
    order_date = request.POST.get("orderDate", None)
    order_price = request.POST.get("orderPrice")
    order_merchandiser_id = request.POST.get("merchandiser")
    order_mail_link = request.POST.get("gmailLink")
    merchandiser = Merchandiser.objects.get(id=order_merchandiser_id)
    order = Order()
    order.merchandiser = merchandiser
    order.order_name = order_name
    order.order_date = order_date
    order.order_price = order_price
    order.mail_link = order_mail_link
    order_detail = OrderDetail()
    try:
        order.save()
        order_detail.order = order
        order_detail.save()
        content = "success"
    except Exception as e:
        print e.message
        content = e.message
    return HttpResponse(content)


