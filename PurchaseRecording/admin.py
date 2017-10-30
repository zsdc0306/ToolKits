from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CreditCard)
admin.site.register(Order)
admin.site.register(Merchandiser)
admin.site.register(OrderDetail)
admin.site.register(EarningDetail)
admin.site.register(Address)
admin.site.register(PaymentInfo)
admin.site.register(CashBackSite)