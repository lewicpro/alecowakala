from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
from django.utils import timezone
# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework import generics
from rest_framework.views import APIView
import datetime
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json

class CashInView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CashInSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return CashIn.objects.filter(company=company).order_by('-pk')

class CashOutView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CashOutSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return CashOut.objects.filter(company=company).order_by('-pk')
class DebtsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = DebtsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Debts.objects.filter(company=company).order_by('-pk')

class InOfficeView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = InOfficeSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return InOffice.objects.filter(company=company).order_by('-pk')

class ProcessorsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProcessorsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Processors.objects.filter(company=company).order_by('-pk')

class CapitalView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CapitalSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Capital.objects.filter(company=company).order_by('-pk')

class ClientsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Clients.objects.filter(company=company).order_by('-pk')
class MyEmployeeView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Clients.objects.filter(company=company).order_by('-pk')

class ClientpersonalView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		username=self.kwargs['username']
		return Clients.objects.filter(officer=username).order_by('-pk')

class DeleteView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = DeleteSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		username=self.kwargs['username']
		return Delete.objects.filter(officer=username).order_by('-pk')

	def post(self, request, *args, **kwargs):
		section=self.kwargs['action']
		pk=self.kwargs['pk']
		data = request.data
		serializer = DeleteSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			if section =='cashin':
				delete=CashIn.objects.filter(pk=pk).delete()
			if section =='cashout':
				delete=CashOut.objects.filter(pk=pk).delete()
			if section =='voucher':
				delete=Voucher.objects.filter(pk=pk).delete()
			if section =='inoffice':
				delete=InOffice.objects.filter(pk=pk).delete()
			if section =='outoffice':
				delete=OutOffice.objects.filter(pk=pk).delete()
			if section =='checkpayment':
				delete=CheckPayment.objects.filter(pk=pk).delete()
			if section =='pendingin':
				delete=PendingIn.objects.filter(pk=pk).delete()
			if section =='pendingout':
				delete=PendingOut.objects.filter(pk=pk).delete()
			if section =='service':
				delete=Processors.objects.filter(pk=pk).delete()
			if section =='capital':
				delete=Capital.objects.filter(pk=pk).delete()
			if section =='balance':
				delete=Balance.objects.filter(pk=pk).delete()
			if section =='clients':
				delete=Clients.objects.filter(pk=pk).delete()
			if section =='debts':
				delete=Debts.objects.filter(pk=pk).delete()
			
			mon = serializer.save()
			return Response(serializer.validated_data)

class ReportCashInView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CashInSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		value=self.kwargs['value']
		# if status=='daily':
		print('imepita ')
		return CashIn.objects.filter(company=company, service__contains=value).order_by('-pk')

	# def post(self, request, *args, **kwargs):
	# 	status=self.kwargs['status']
	# 	compnay=self.kwargs['company']
	# 	data = request.data
	# 	serializer = DeleteSerializer(data=data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		mon = serializer.save()
	# 		return Response(serializer.validated_data)
class ReportCashOutView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CashOutSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		value=self.kwargs['value']
		# if status=='daily':
		print('imepita ')
		return CashOut.objects.filter(company=company, service__contains=value).order_by('-pk')

class ReportPendingOutView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PendingOutSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		value=self.kwargs['value']
		# if status=='daily':
		print('imepita ')
		return PendingOut.objects.filter(company=company, service__contains=value).order_by('-pk')

	# def post(self, request, *args, **kwargs):
	# 	status=self.kwargs['status']
	# 	compnay=self.kwargs['company']
	# 	data = request.data
	# 	serializer = DeleteSerializer(data=data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		mon = serializer.save()
	# 		return Response(serializer.validated_data)
class ReportPendingInView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PendingInSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		value=self.kwargs['value']
		# if status=='daily':
		print('imepita ')
		return PendingIn.objects.filter(company=company, service__contains=value).order_by('-pk')

	# def post(self, request, *args, **kwargs):
	# 	status=self.kwargs['status']
	# 	compnay=self.kwargs['company']
	# 	data = request.data
	# 	serializer = DeleteSerializer(data=data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		mon = serializer.save()
	# 		return Response(serializer.validated_data)
class CheckPaymentView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CheckPaymentSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return CheckPayment.objects.filter(company=company).order_by('-pk')
class CheckCashinDate(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CashInSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):

		company=self.kwargs['company']
		time=self.kwargs['time']
		comp=time.split(' ')
		mime=comp[0]
		start=datetime.datetime.strptime(mime, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
		return CashIn.objects.filter(date__icontains=mime).order_by('-pk')
class CheckCashOutDate(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CashOutSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):

		company=self.kwargs['company']
		time=self.kwargs['time']
		comp=time.split(' ')
		mime=comp[0]
		start=datetime.datetime.strptime(mime, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
		return CashOut.objects.filter(date__icontains=mime).order_by('-pk')
class CheckPendingInDate(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PendingInSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		company=self.kwargs['company']
		time=self.kwargs['time']
		comp=time.split(' ')
		mime=comp[0]
		start=datetime.datetime.strptime(mime, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
		return PendingIn.objects.filter(date__icontains=mime).order_by('-pk')
class CheckPendingOutDate(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PendingOutSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		company=self.kwargs['company']
		time=self.kwargs['time']
		comp=time.split(' ')
		mime=comp[0]
		start=datetime.datetime.strptime(mime, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
		return PendingOut.objects.filter(date__icontains=mime).order_by('-pk')

class PendingInView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PendingInSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return PendingIn.objects.filter(company=company).order_by('-pk')

class PendingOutView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PendingOutSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return PendingOut.objects.filter(company=company).order_by('-pk')
	
class OutOfficeView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = OutOfficeSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return OutOffice.objects.filter(company=company).order_by('-pk')
	
class VoucherView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = VoucherSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Voucher.objects.filter(company=company).order_by('-pk')

class BalanceView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BalanceSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return Balance.objects.filter(company=company).order_by('-pk')
	

class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			# usere = serializer.validated_data['email']
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CreateUserView(generics.CreateAPIView):
	model = get_user_model()
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer
