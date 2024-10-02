from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["paid_course", "paid_lesson", "payment_method",]
    ordering_fields = ["payment_date", "payment_amount",]

    serializer_class = PaymentsSerializer
