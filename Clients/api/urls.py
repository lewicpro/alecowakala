"""back_moneyvendor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import  *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name='Clients'
urlpatterns = [
    # path('', admin.site.urls),
    # url(r'^customer/$', TokenValidatorAPIView.as_view(), name='token'),
    url(r'toke_pro/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^signup/$', CreateUserView.as_view(), name='signup'),
    url(r'^clients/$', ClientsView.as_view(), name='clients'),
    url(r'^myemployee/(?P<company>.+)/$', MyEmployeeView.as_view(), name='clients'),
    url(r'^cashout/(?P<company>.+)/$', CashOutView.as_view(), name='cashout'),
    url(r'^clientsdata/(?P<username>.+)/$', ClientpersonalView.as_view(), name='clientsdata'),
    # url(r'^clientsreport/(?P<company>.+)/(?P<status>.+)/$', ReportCashInView.as_view(), name='report-client'),
    url(r'^searchcashout/(?P<company>.+)/(?P<value>.+)/$', ReportCashOutView.as_view(), name='report-client'),
    url(r'^searchcashin/(?P<company>.+)/(?P<value>.+)/$', ReportCashInView.as_view(), name='report-client'),
    url(r'^searchpendingout/(?P<company>.+)/(?P<value>.+)/$', ReportPendingOutView.as_view(), name='report-client'),
    url(r'^searchpendingin/(?P<company>.+)/(?P<value>.+)/$', ReportPendingInView.as_view(), name='report-client'),
    url(r'^delete/(?P<action>.+)/(?P<pk>.+)/$', DeleteView.as_view(), name='clientsdata'),
    url(r'^cashin/(?P<company>.+)/$', CashInView.as_view(), name='cashin'),
    url(r'^voucher/(?P<company>.+)/$', VoucherView.as_view(), name='voucher'),
    url(r'^momis/checkdate/(?P<time>.+)/(?P<company>.+)/$', CheckCashinDate.as_view(), name='today'),
    url(r'^cahoutchek/checkdate/(?P<time>.+)/(?P<company>.+)/$', CheckCashOutDate.as_view(), name='today'),
    url(r'^pendingincheck/checkdate/(?P<time>.+)/(?P<company>.+)/$', CheckPendingInDate.as_view(), name='today'),
    url(r'^pendingOutcheck/checkdate/(?P<time>.+)/(?P<company>.+)/$', CheckPendingOutDate.as_view(), name='today'),
    url(r'^inoffice/(?P<company>.+)/$', InOfficeView.as_view(), name='inoffice'),
    url(r'^outoffice/(?P<company>.+)/$', OutOfficeView.as_view(), name='outoffice'),
    url(r'^checkpayment/(?P<company>.+)/$', CheckPaymentView.as_view(), name='checkpaument'),
    url(r'^pendingin/(?P<company>.+)/$', PendingInView.as_view(), name='pendingin'),
    url(r'^pendingout/(?P<company>.+)/$', PendingOutView.as_view(), name='pendingout'),
    url(r'^processors/(?P<company>.+)/$', ProcessorsView.as_view(), name='processors'),
    url(r'^capital/(?P<company>.+)/$', CapitalView.as_view(), name='capital'),
    url(r'^balance/(?P<company>.+)/$', BalanceView.as_view(), name='balance'),
    url(r'^debts/(?P<company>.+)/$', DebtsView.as_view(), name='debts'),
    # path('api-auth/', include('rest_framework.urls')),
    # url(r'^postClient/(?P<username>.+)/$', Job_requestsView.as_view(), name='data'),
]
