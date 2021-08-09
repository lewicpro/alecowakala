from django.contrib import admin
from .models import *


# Register your models here.
class CashOutAdmin(admin.ModelAdmin):
    search_fields = ('date', 'user', 'name', 'service', 'transactionid', 'commission', 'salio')
            
    list_display=['date', 'user', 'name', 'service', 'transactionid', 'commission', 'salio']

class VoucherAdmin(admin.ModelAdmin):
    search_fields = ('date', 'user', 'name', 'service', 'transactionid', 'commission', 'salio')
            
    list_display=['user', 'date', 'name', 'service', 'transactionid', 'commission', 'salio']
class CashInAdmin(admin.ModelAdmin):
    search_fields = ('user', 'name', 'service', 'transactionid', 'commission', 'salio')
            
    list_display=['user', 'date', 'name', 'service', 'transactionid', 'commission', 'salio']

class InOfficeAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'name', 'amount', 'company', 'transactionid', 'description',)
            
    list_display=['user','date', 'name', 'amount', 'company', 'transactionid', 'description',]

class OutOfficeAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'name', 'amount', 'company', 'transactionid', 'description',)
            
    list_display=['user','date', 'name', 'amount', 'company', 'transactionid', 'description',]

class CheckPaymentAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'name', 'amount', 'company', 'transactionid', 'description',)
            
    list_display=['user','date', 'name', 'amount', 'company', 'transactionid', 'description',]

class PendingInAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'name', 'amount', 'company', 'transactionid', 'description',)
            
    list_display=['user','date', 'name', 'amount', 'company', 'transactionid', 'description',]

class PendingOutAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'name', 'amount', 'company', 'transactionid', 'description',)
            
    list_display=['user','date', 'name', 'amount', 'company', 'transactionid', 'description',]

class ProcessorsAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'service_name', 'description',)
            
    list_display=['user','date', 'service_name','description',]

class CapitalAdmin(admin.ModelAdmin):
    search_fields = ('user', 'date', 'service_name', 'description',)
            
    list_display=['user','date', 'service_name','description',]
class BalanceAdmin(admin.ModelAdmin):
    search_fields = ('date', 'user', 'processor', 'amount', 'commission', 'officer', 'company', 'description',)
            
    list_display=['date', 'user', 'processor', 'amount', 'commission', 'officer', 'company', 'description',]
class ClientsAdmin(admin.ModelAdmin):
    search_fields = ('date', 'user',  'fullname', 'email', 'commission', 'officer', 'service', 'transactionid', 'privillages', 'company')
            
    list_display=['date', 'user',  'fullname', 'email', 'commission', 'officer', 'service', 'transactionid', 'privillages', 'company']

admin.site.register(CashOut, CashOutAdmin)
admin.site.register(CashIn, CashInAdmin)
admin.site.register(Voucher, VoucherAdmin)
admin.site.register(InOffice, InOfficeAdmin)
admin.site.register(OutOffice, OutOfficeAdmin)
admin.site.register(CheckPayment, CheckPaymentAdmin)
admin.site.register(PendingIn, PendingInAdmin)
admin.site.register(PendingOut, PendingOutAdmin)
admin.site.register(Processors, ProcessorsAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Clients, ClientsAdmin)