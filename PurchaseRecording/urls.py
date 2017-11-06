from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^credmanagement$', views.credit_card_management, name='ccmanagement'),
    url(r'^orders$', views.orders, name='orders'),
    url(r'^orders/(?P<order_id>[0-9]*)$', views.get_order_detail, name="orderdetail"),
    url(r'^ordersrecord$', views.create_order_record_page, name="ordercreate"),
    url(r'^GCmanagement$', views.gift_card_management, name='gcmanagement'),
    # url(r'^login/(?P<username>[A-Za-z0-9]+)/AccountDetail.html$', views.viewDetail, name= "AccountDetail"),
    # url(r'^AccountDetail.html$', views.login, name='login'),
    # url(r'^create/(?P<username>[A-Za-z0-9]+)/$', views.addAccount, name= "addAccount"),
    url(r'^addRecord/submit/',views.create_record,name="addRecord"),
    # url(r'^form/submit/', views.upgradeAccount, name="upgradeAccount"),
    # url(r'^form/record/delete/', views.deleteRecord, name="deleteRecord"),
    # url(r'^form/record/update/', views.updateRecord, name="updateRecord"),
    # url(r'^form/record/add/', views.createRecord, name="createRecord"),
    # url(r'^form/record/generatechart/', views.genChart, name="genChart"),
    # url(r'^form/record/export/', views.exportCSV, name="exportCSV"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
