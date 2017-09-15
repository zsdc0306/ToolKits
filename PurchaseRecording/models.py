from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.db import models

# Create your models here.
order_status_type = (
    (0, 'ordered'),
    (1, 'shipped'),
    (2, 'canceled'),
    (3, 'delivered'),
    (4, 'picked')
)
carrier_type = (
    (0, 'Ups'),
    (1, 'Fedex'),
    (2, 'USPS'),
    (3, 'other'),
    (9, 'undefined')
)


class CreditCard(models.Model):
    card_num = models.CharField(unique=True, primary_key=True, max_length=16)
    sec_code = models.CharField(max_length=4, default="0000")
    card_name = models.CharField(unique=True, max_length=10)
    card_exp_date = models.DateField(datetime.now().date()+timedelta(days=365*5))
    def __unicode__(self):
        return self.card_name


class CashBackSite(models.Model):
    site_url = models.CharField(unique=True, max_length=20, error_messages={'unique': "site already existed"})
    site_name = models.CharField(unique=True, primary_key=True, max_length= 10)


class Merchandiser(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    url = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name


class Order(models.Model):
    order_inner_id = models.AutoField(primary_key=True, max_length=20)
    order_name = models.CharField(max_length=20)
    merchandiser = models.ForeignKey(Merchandiser)
    order_date = models.DateField()
    order_status = models.IntegerField(choices=order_status_type, default=0)
    order_price = models.FloatField(default=0.0)
    def __unicode__(self):
        return self.order_name


class EarningDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    cashback_site_cashback = models.FloatField(default=0.0)
    credit_card_cashback = models.FloatField(default=0.0)
    other_cashback = models.FloatField(default=0.0)
    note = models.CharField(blank=True, max_length=200)
    earing_num = models.FloatField(default=0)
    def __unicode__(self):
        return self.order_id.order_name


class Address(models.Model):
    addr_name = models.CharField(max_length=10)
    addr_zip = models.CharField(max_length=10)
    def __unicode__(self):
        return self.addr_name


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_name = models.CharField(max_length=20)
    item_price = models.FloatField(default=0.0)
    item_num = models.IntegerField(default=1)
    carrier =models.IntegerField(choices=carrier_type,default=9)
    tracking_num = models.CharField(max_length=20,default="undefined")
    deliver_address = models.ForeignKey(Address)
    credit_card = models.ForeignKey(CreditCard)
    earning = models.ForeignKey(EarningDetail)
    def __unicode__(self):
        return self.order_name


class PaymentInfo(models.Model):
    payment_id = models.CharField(max_length=20)
    payment_date = models.DateField()
    amount = models.FloatField()


class GiftCard(models.Model):
    card_id = models.CharField(primary_key=True, max_length=10)
    brand = models.ForeignKey(Merchandiser, on_delete=models.CASCADE)
    value = models.FloatField()
    card_num = models.CharField(max_length=30)
    pin_num = models.CharField(max_length=10)
    is_used = models.BooleanField()
    remain_value = models.FloatField(default=value)
    expire_date = models.DateField(default=datetime.now().date()+timedelta(days=365))
