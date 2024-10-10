from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.viewsets import ModelViewSet

from payments.models import Payments
from payments.serializers import PaymentsSerializer



# class PaymentsViewSet(ModelViewSet):
#     queryset = Payments.objects.all()
#     serializer_class = PaymentsSerializer
#
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = [
#         "paid_course",
#         "paid_lesson",
#         "payment_method",
#     ]
#     ordering_fields = [
#         "payment_date",
#         "payment_amount",
#     ]


class PaymentsCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method', 'course', 'lesson']
    ordering_fields = ['payment_date']


class PaymentsRetrieveAPIView(RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsUpdateAPIView(UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyAPIView(DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
