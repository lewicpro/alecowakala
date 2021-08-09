from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
from django.utils import timezone
# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework import generics
from rest_framework.views import APIView
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

class ClientpersonalView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ClientsSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		username=self.kwargs['username']
		return Clients.objects.filter(officer=username).order_by('-pk')

class CheckPaymentView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CheckPaymentSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		company=self.kwargs['company']
		return CheckPayment.objects.filter(company=company).order_by('-pk')

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
