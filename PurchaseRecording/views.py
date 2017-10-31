from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    order_status_percentage = get_status_summary()
    print order_status_percentage
    output = {
        "status": order_status_percentage
    }
    return HttpResponse(template.render(output,request))


def get_status_summary(date=None):
    total_order = Order.objects.filter().count().__float__()
    ordered_num = Order.objects.filter(order_status=0).count().__float__()
    shipped_num = Order.objects.filter(order_status=1).count().__float__()
    canceled_num = Order.objects.filter(order_status=2).count().__float__()
    delivered_num = Order.objects.filter(order_status=3).count().__float__()
    picked_num = Order.objects.filter(order_status=4).count().__float__()
    percentage = {"ordered": ordered_num / total_order, "shipped": shipped_num / total_order,
                  "canceled": canceled_num / total_order, "delivered": delivered_num / total_order,
                  "picked": picked_num / total_order}
    return percentage



def credit_card_management(request):
    template = loader.get_template('credmanagement.html')
    output = {
    }
    return HttpResponse(template.render(output, request))


def orders(request):
    template = loader.get_template('orders.html')
    orders = Order.objects.filter().order_by("-order_date")
    # use get_order_status_display instead of this
    # for order in orders:
    #     order.order_status = order_status_type[order.order_status][1]
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
    credit_card = CreditCard.objects.filter()
    address = Address.objects.filter()
    cash_back = CashBackSite.objects.filter()
    output = {
        'merchandisers': merchandiser,
        'creditcards': credit_card,
        'addresses': address,
        'cashbacks': cash_back
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
    # set order_detail attributes
    item_price = request.POST.get("itemPrice")
    item_num = request.POST.get("itemNum")
    pay_method_val = request.POST.get("payMethod")
    deliver_addr = request.POST.get("deliverAddress")
    cash_back_site = request.POST.get("cashbackSite")
    cash_back_rate = request.POST.get("cashbackRate")
    cashback = float(cash_back_rate)/100 * float(order_price)
    order_detail = OrderDetail()
    try:
        order.save()
    except Exception as e:
        print e.message
        return HttpResponse(e.message)
    order_detail = set_order_detail(order_detail, order, item_price, item_num, pay_method_val,
                                    deliver_addr, cash_back_site, cashback)
    try:
        order_detail.save()
    except Exception as e:
        return HttpResponse(e.message)
    # TODO
    # use banner instead of HTTP response
    template = loader.get_template("orders.html")
    return HttpResponse("success")


def set_order_detail(order_detail, order, item_price=None, item_num=None, pay_method_val=9,
                     deliver_addr=None, cash_back_site=None, cash_back=0.0):
    pay_type = pay_method_val if pay_method_val == 1 or pay_method_val == 8 or pay_method_val == 9 else 0
    if item_price:
        order_detail.item_price = item_price
    if item_num:
        order_detail.item_num = item_num
    order_detail.pay_method = pay_type
    if pay_type == 0:
        print pay_method_val
        credit_card = CreditCard.objects.get(card_num=pay_method_val)
        order_detail.credit_card = credit_card
    if deliver_addr:
        address = Address.objects.get(id=deliver_addr)
        order_detail.deliver_address = address
    if cash_back_site:
        cb_site = CashBackSite.objects.get(site_name=cash_back_site)
        earning = EarningDetail()
        earning.cashback = cb_site
        earning.cashback_site_cashback = cash_back
        earning.order = order
        earning.save()
        order_detail.earning = earning
    order_detail.order = order
    return order_detail



