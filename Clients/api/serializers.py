from rest_framework import serializers
from ..models import *
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ValidationError, SerializerMethodField
from django.db.models import Q
User = get_user_model()



class CashOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashOut
        fields=['date', 'user', 'name', 'payment', 'service', 'company', 'officer', 'transactionid', 'commission', 'salio']

class CashInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashIn
        fields=['date', 'user', 'name', 'officer', 'service', 'company',  'payment', 'transactionid', 'commission', 'salio']

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields=['date', 'user', 'name', 'officer', 'company', 'service',  'payment', 'transactionid', 'commission', 'salio']
class InOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InOffice
        fields=['date', 'user',  'name', 'amount', 'officer', 'company', 'service', 'transactionid', 'description',]
class OutOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOffice
        fields=['date', 'user',  'name', 'amount', 'officer', 'company', 'service', 'transactionid', 'description',]
class CheckPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckPayment
        fields=['date', 'user',  'name', 'amount', 'officer', 'company', 'service', 'transactionid', 'description',]

class PendingInSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingIn
        fields=['date', 'user',  'name', 'amount', 'officer', 'company', 'service', 'transactionid', 'description',]
class PendingOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingOut
        fields=['date', 'user',  'name', 'amount', 'officer', 'company', 'service', 'transactionid', 'description',]
class ProcessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processors
        fields=['date', 'user', 'service_name', 'officer', 'company', 'description',]

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields=['date', 'user', 'amount', 'service_name', 'commission', 'officer', 'company', 'description',]


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields=['date', 'user', 'processor', 'amount', 'commission', 'officer', 'company', 'description',]

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields=['date', 'user', 'fullname', 'email', 'commission', 'officer', 'service', 'transactionid', 'privillages', 'company', 'Nationality']


class UserLoginSerializer(serializers.ModelSerializer):
    # token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True)
    # email = EmailField(label="email ", allow_blank=True)
    
    class Meta:
        model = User
        fields =[
            'pk', 
            'username',
            # 'email',
            'password',
            # 'token',
        ]

        extra_kwargs = {"password":
                                {"write_only": True}
                                }

    def validate(self, data):
        user_obj =None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or Email is required to login")

        user =User.objects.filter(
            Q(email=email) |
            Q(username=username)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password")
        data["token"] = "SOME RANDOM TO"


        return data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Confirm pasword")


    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model =User
        fields = [
            'pk', 
            'username',
            'password',
            'password2',
            'email'
           ]


    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password")
        # username = data.get("username", None)
        password2 = value
        if password != password2:
            raise ValidationError('passwords must be the same')
        return value


