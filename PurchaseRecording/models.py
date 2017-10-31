from __future__ import unicode_literals
from datetime import datetime, timedelta
from django.utils import timezone

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

pay_method = (
    (0, "Credit Card"),
    (1, "Gift Card"),
    (8, "other"),
    (9, "undefined")
)



class CreditCard(models.Model):
    card_num = models.CharField(unique=True, primary_key=True, max_length=16)
    sec_code = models.CharField(max_length=4, default="0000")
    card_name = models.CharField(unique=True, max_length=10)
    card_exp_date = models.DateField(default=timezone.now().date() + timedelta(days=365 * 5))

    def __unicode__(self):
        return self.card_name


class CashBackSite(models.Model):
    site_url = models.CharField(unique=True, max_length=50, error_messages={'unique': "site already existed"})
    site_name = models.CharField(unique=True, primary_key=True, max_length=20)
    balance = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.site_name


class Merchandiser(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    reward = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.name


class GiftCard(models.Model):
    brand = models.ForeignKey(Merchandiser, on_delete=models.CASCADE)
    value = models.FloatField()
    card_num = models.CharField(max_length=30)
    pin_num = models.CharField(max_length=10)
    is_used = models.BooleanField()
    remain_value = models.FloatField(default=value)
    expire_date = models.DateField(default=timezone.now().date() + timedelta(days=365))

    def __unicode__(self):
        return self.brand.name + str(self.remain_value)


class Order(models.Model):
    order_name = models.CharField(max_length=20)
    merchandiser = models.ForeignKey(Merchandiser)
    order_date = models.DateField()
    order_status = models.IntegerField(choices=order_status_type, default=0)
    order_price = models.FloatField(default=0.0)
    mail_link = models.CharField(max_length=100, default="")

    def __unicode__(self):
        return self.order_name


class EarningDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cashback_site_cashback = models.FloatField(default=0.0)
    cashback = models.ForeignKey(CashBackSite, null=True, blank=True)
    credit_card_cashback = models.FloatField(default=0.0)
    other_cashback = models.FloatField(default=0.0)
    note = models.CharField(blank=True, max_length=200)
    earing_num = models.FloatField(default=0)

    def __unicode__(self):
        return self.order.order_name


class Address(models.Model):
    addr_name = models.CharField(max_length=20)
    addr_zip = models.CharField(max_length=10)
    addr_line1 = models.CharField(max_length=50, blank=True)
    addr_line2 = models.CharField(max_length=50, blank=True)
    addr_city = models.CharField(max_length=20, blank=True)
    addr_state = models.CharField(max_length=10, blank=True)
    is_default = models.BooleanField(default=False)

    def __unicode__(self):
        return self.addr_name


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_price = models.FloatField(default=0.0)
    item_num = models.IntegerField(default=1, null=True, blank=True)
    carrier = models.IntegerField(choices=carrier_type, default=9)
    tracking_num = models.CharField(max_length=20, default="undefined")
    deliver_address = models.ForeignKey(Address, default=2)
    pay_method = models.IntegerField(choices=pay_method, default=9)
    gift_card = models.ForeignKey(GiftCard, null=True, blank=True)
    credit_card = models.ForeignKey(CreditCard, null=True)
    earning = models.ForeignKey(EarningDetail, null=True, blank=True)

    def __unicode__(self):
        return self.order.order_name


class PaymentInfo(models.Model):
    payment_date = models.DateField(default=timezone.now)
    paid_to = models.ForeignKey(CreditCard, null=True, blank=True)
    amount = models.FloatField()

    def __unicode__(self):
        return str(self.payment_date)

