from django.shortcuts import render

# I decided to use generics because it has
# all the configs to make a CRUD API like this 
from rest_framework import generics

from .models import Reservation, PaymentMethod, Status, Client
from .serializers import ClientSerializer, ReservationSerializer, PaymentMethodSerializer, StatusSerializer

# Reservation endpoints

# All the reservations 

class ReservationList(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        # Get all the data
        queryset = Reservation.objects.all()

        # Get the payment Method and filter the query
        payment_method = self.request.query_params.get('payment_method')
        status = self.request.query_params.get('status')
        client = self.request.query_params.get('client')

        # Filtering the query based on the query params
        if payment_method is not None and status is not None and client is not None:
            queryset = queryset.filter(payment_method=payment_method)
            queryset = queryset.filter(status=status)
            queryset = queryset.filter(client=client)

        return queryset

# Single reservation endpoints

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

# Payment Method endpoints

# All the payment methods
class PaymentMethodList(generics.ListCreateAPIView):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()

# single payment method

class PaymentMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()

# Status endpoints

# All the status list
class StatusList(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

# Single status
class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

# Client endpoints

# All the client list
class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

# Single client
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()