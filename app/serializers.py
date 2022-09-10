from rest_framework import serializers
from .models import Reservation, PaymentMethod, Status, Client


# In this case, I decided to use all the fields

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('__all__')

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('__all__')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('__all__')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')